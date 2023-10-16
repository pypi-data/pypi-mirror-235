# python-runner

Python environment setup and runner execution.

## Development

### Preparations

```shell
# Win
py -3.9 -m venv ./.venv
# *nix
python -m venv ./.venv
# Win
.\.venv\Scripts\activate
# *nix
source ./.venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For developing depending project/module, dependency can be added into **requirements.txt** as:

    python-commons @ file:///C:/sources/setmy.info/submodules/python-commons

### PyCharm

"File" -> "Settings" -> Python Integrated Tools -> Default test runner: Unittest

Running tests have a problem: working directory has to be set for tests.

### Run unit tests

```shell
python -m unittest discover -s ./test
```

### Run integration tests

```shell
python -m unittest discover -s ./test -p it_*.py
```

### All tests

```shell
python -m unittest discover -s ./test && python -m unittest discover -s ./test -p it_*.py
```

### Update version info

```shell
# Win
set NAME=smi_python_runner
set VERSION=1.2.0
# *nix
NAME=smi_python_runner
VERSION=1.2.0
# Win
python -m smi_python_commons.scm_version %NAME% %VERSION%
# *nix
python -m smi_python_commons.scm_version ${NAME} ${VERSION}
git add ./${NAME}/project.py
git commit -m "project.py updated"
git push
```

## Deploy

```shell
python setup.py sdist bdist_wheel
twine upload dist/*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags
```

## Release

1. Update version info
2. Deploy

```shell
python setup.py sdist bdist_wheel && twine upload dist/*
```

## Usage

**application.py**

```python
from smi_python_commons.arguments.argument import Argument

from smi_python_runner.services.arguments_register_service import arguments_register_service
from smi_python_runner.services.runner_register_service import runner_register_service
from test.empty_runner import EmptyRunner


def register():
    arguments_register_service.register(Argument('example', 'e', str, 'Example', True))
    empty_runner = EmptyRunner()
    runner_register_service.register(empty_runner)
```

**empty_runner.py**

```python
from smi_python_commons.config.application import Application


class EmptyRunner:

    def __init__(self):
        self.name = "empty-runner"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        return 0
```

**runner-x_sub-x.py**

```python
import logging

from smi_python_commons.config.application import Application

from smi_python_runner.services.runner_register_service import runner_register_service

log = logging.getLogger(__name__)

logging.info("Loaded module")


class RunnerAbc:

    def __init__(self):
        self.name = "runner-abc"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        return 0


def init():
    logging.info("Init module")
    runner_register_service.register(RunnerAbc())
```
