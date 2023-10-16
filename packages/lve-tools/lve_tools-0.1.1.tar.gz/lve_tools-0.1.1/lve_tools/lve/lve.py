import json
import os
import time
from enum import Enum
from typing import Any, List, Union, Optional
import inspect

import openai
import lmql
from lve.errors import *

from pydantic import BaseModel, RootModel, model_validator, ValidationError
from pydantic.dataclasses import dataclass

def split_instance_args(args, prompt_parameters):
    if prompt_parameters is None:
        return {}, args
    param_values, model_args = {}, {}
    for key in args:
        if key in prompt_parameters:
            param_values[key] = args[key]
        else:
            model_args[key] = args[key]
    return param_values, model_args

def prompt_to_openai(prompt):
    messages = []
    for msg in prompt:
        messages += [{"content": msg.content, "role": str(msg.role)}]
    return messages

class Role(str, Enum):
    user = "user"
    assistant = "assistant"
    system = "system"

    def __str__(self):
        return self.value

@dataclass
class Message:
    content: str
    role: Role

class TestInstance(BaseModel):

    args: dict[str, Any]
    response: str
    passed: bool = True
    author: Optional[str] = None
    run_info: dict

def get_prompt(prompt):
    if isinstance(prompt, str):
        return [Message(content=prompt, role=Role.user)]
    else:
        assert False

class LVE(BaseModel):
    """
    Base class for an LVE test case, as represented
    by a directory with a test.json file.
    """
    name: str
    category: str
    path: str
    
    description: str
    model: str
    checker_args: dict[str, Any]
    author: Optional[str] = None

    prompt_file: Optional[str] = None
    prompt: Union[str, list[Message]] = None
    prompt_parameters: Union[list[str], None] = None

    # names of existing instance files (instances/*.json)
    instance_files: List[str]

    def model_post_init(self, __context: Any) -> None:
        super().model_post_init(__context)
        if self.prompt_file is not None:
            # interpreter prompt_file relative to test path if it exists
            if os.path.exists(os.path.join(self.path, self.prompt_file)):
                self.prompt_file = os.path.join(self.path, self.prompt_file)
        
            with open(self.prompt_file, 'r') as fin:
                contents = fin.read()
                if contents == "<please fill in>":
                    self.prompt = None
                else:
                    self.prompt = get_prompt(contents)
        return self

    @model_validator(mode='after')
    def verify_test_config(self):
        if self.prompt_file is not None:
            assert self.prompt_file.endswith(".prompt"), "Prompt file should end with .prompt"
            if not os.path.exists(self.prompt_file):
                raise ValueError("Prompt file does not exist!")
        
        # at this point, self.prompt_file has been already loaded
        if self.prompt is None:
            raise ValueError(f"Must specify a prompt in {self.path}/test.json. Either fill in the test.prompt file or specify a prompt directly in test.json.")

        if 'checker_name' not in self.checker_args:
            raise ValueError(f"You must specify a checker_name under chercker_args in in {self.path}/test.json.")

        if self.checker_args['checker_name'] == "<please fill in>":
            raise ValueError(f"You must specify a checker_name in {self.path}/test.json.")

        if self.prompt_parameters is not None and len(self.prompt_parameters) == 1 and self.prompt_parameters[0] == "<please fill in>":
            raise ValueError(f"'prompt_parameters' in {self.path}/test.json has not been filled in yet!")

        return self

    def fill_prompt(self, param_values):
        new_prompt = []
        for msg in self.prompt:
            content, role = msg.content, msg.role
            new_msg = Message(content=content.format(**param_values), role=role)
            new_prompt.append(new_msg)
        return new_prompt
    
    async def run(self, author=None, verbose=False, engine='openai', **kwargs):
        if engine == 'lmql':
            return await self.run_with_lmql(author=author, verbose=verbose, **kwargs)
        else:
            assert engine == 'openai', f"Only 'lmql' and 'openai' are supported as inference engines, not '{engine}'"

        run_info = self.get_run_info()

        param_values, model_args = split_instance_args(kwargs, self.prompt_parameters)
        prompt = self.fill_prompt(param_values)
        prompt_openai = prompt_to_openai(prompt)

        # for now just remove the openai/ prefix
        model = self.model
        if model.startswith("openai/"):
            model = model[len("openai/"):]

        if verbose:
            for msg in prompt:
                print(f"[{msg.role}] {msg.content}")

        completion = await openai.ChatCompletion.acreate(
            model=model,
            messages=prompt_openai,
            **model_args,
        )
        # TODO: Support multiple responses
        response = completion.choices[0]["message"]["content"]

        checker = self.get_checker()
        is_safe = checker.is_safe(prompt, response, param_values)

        return TestInstance(
            author=author,
            args=kwargs,
            response=response,
            run_info=run_info,
            passed=is_safe,
        )

    async def run_with_lmql(self, author=None, verbose=False, **kwargs):
        param_values, model_args = split_instance_args(kwargs, self.prompt_parameters)
        prompt = self.fill_prompt(param_values)
        prompt_openai = prompt_to_openai(prompt)

        # make compatible with previous model identifiers
        model = self.model
        if model in ["gpt-4", "gpt-3.5-turbo"]:
            model = "openai/" + model
        
        if verbose:
            for msg in prompt:
                print(f"[{msg.role}] {msg.content}")

        with lmql.traced("LVE.run") as t:
            response = await lmql.generate(prompt_openai, model=model, **model_args, chunk_timeout=60.0)
            certificate = lmql.certificate(t)
        response = response[1:] if response.startswith(" ") else response

        checker = self.get_checker()
        is_safe = checker.is_safe(prompt, response, param_values)

        return TestInstance(
            author=author,
            args={k: v for k, v in kwargs.items() if v is not None},
            response=response,
            run_info=certificate.asdict(),
            passed=is_safe,
        )
    
    async def run_instance(self, instance, engine):
        return await self.run(engine=engine, **instance.args)
    
    def __hash__(self):
        return hash(self.path)

    @classmethod
    def load_from_file(cls, test_path):
        with open(test_path, "r") as fin:
            test_config = json.loads(fin.read())
        return cls(**test_config, test_path=test_path)
    
    @classmethod
    def from_path(cls, path):
        """
        Reads an existing LVE from the given path.
        """
        from lve.repo import get_active_repo

        path = os.path.abspath(path)

        # check if the path exists
        if not os.path.exists(path):
            raise NoSuchLVEError(f"Could not find LVE directory at {path}")
        
        # if the path is a file, we assume it's an instance file
        test_file = os.path.join(path, "test.json")
        if not os.path.exists(test_file):
            raise NoSuchLVEError(f"Could not find LVE test.json file at {test_file}")

        # read the test.json file
        contents = "<failed to read>"
        try:    
            with open(test_file, "r") as f:
                contents = f.read()
                test = json.loads(contents)
        except Exception as e:
            raise InvalidLVEError(f"Could not read LVE test.json file at {test_file}:\n\n{e}\n\n{contents}")
        
        # check if the test.json file is valid
        if "model" not in test:
            raise InvalidLVEError(f"Invalid LVE test.json file at {test_file}: missing 'model' field")
        
        if "description" not in test:
            raise InvalidLVEError(f"Invalid LVE test.json file at {test_file}: missing 'description' field")
        
        # check if LVE has instances/ directory
        instances_dir = os.path.join(path, "instances")
        if os.path.exists(os.path.join(instances_dir)):
            instance_files = os.listdir(instances_dir)
        else:
            instance_files = []

        # finally derive name and category from path
        repo = get_active_repo()
        repo_path = os.path.relpath(path, repo.path)

        # with repository/ prefix, category is the first directory
        category = repo_path.split("/")[1]
        
        # name is the last directory
        path_after_category = repo_path.split("/")[2:]
        if len(path_after_category) > 1:
            # for <category>/<name>/<model> paths
            name = path_after_category[0]
        else:
            # for <category>/<name> paths
            name = path_after_category[-1]

        if "prompt" not in test:
            test["prompt_file"] = os.path.join(path, "test.prompt")
            if not os.path.exists(test["prompt_file"]):
                raise InvalidLVEError(f"Invalid LVE test.json file at {test_file}: prompt not specified and test.prompt does not exist")

        try:
            return cls(
                name=name,
                category=category,
                path=path,
                instance_files=instance_files,
                **test
            )
        except ValidationError as e:
            raise InvalidLVEError(f"Failed to instantiate LVE from {test_file}:\n\n{e}\n")

    def get_checker(self):
        from lve.checkers import get_checker

        checker_args = self.checker_args.copy()
        checker_name = checker_args.pop("checker_name")
        checker_cls = get_checker(checker_name)

        sig = inspect.signature(checker_cls)
        for param, param_value in sig.parameters.items():
            if param not in checker_args and param_value.default is param_value.empty:
                raise ValueError(f"Checker {checker_name} requires parameter '{param}' but it was not specified in {self.path}/test.json.")

        return checker_cls(**checker_args)
    
    def contains(self, file):
        return os.path.abspath(file).startswith(os.path.abspath(self.path))

    def get_run_info(self):
        return {
            "openai": openai.__version__,
            "timestamp": time.ctime(),
        }

