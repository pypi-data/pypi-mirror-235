# python-tbi-runner

Training Backlog Item file parser

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
set VERSION=1.0.0
# *nix
NAME=smi_python_runner
VERSION=1.0.0
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

## TODO

```python
# from smi_python_tbi_parser.tbi import parse_tbi
# '--smi-tbi-file', './test/resources/tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml',
# arguments_register_service.register(Argument('smi-tbi-file', 't', parse_tbi, 'TBI yaml to be used', True), )
```

**tbi-376bdfaa-1195-11ee-be56-0242ac120002.yaml**

```yaml
name: TBI name
description: TBI description
materials:
    - example.doc
    - https://example.com/document
    - url/uri/path/to/bpmn/file.bpmn (don't repeat, if it is already mentioned in tbi_process_uri)
external_processing_engine:
    type: Camunda (can be missing, for passing directly to Jenkins)
    process_id: MLSprint (can be missing, for passing directly to Jenkins)
    config:
        tbi_process_uri: url/uri/path/to/bpmn/file.bpmn (can be missing, for passing directly to Jenkins)
        jenkins_pipeline:
            tbi_vcs_url: https://example.com/tbi/git/repo/with/Jenkinsfile/pipeline.git  (can be missing, Jenkins already have pipeline execution configured)
            tbi_dvc_path: path/to/dvc (ML software config can also be there, because config is also data)
            tbi_code_vcs_path: path/to/dvc_code (ML software to build, or use tbi_training_command and tbi_testing_command)
            tbi_training_command: command (to execute for training)
            tbi_validating_command: command (to execute for validating)
            tbi_testing_command: command (to execute for testing)
            tbi_config_vcs_path: path/to/config (ML software config to use, can be unset)
            # (default is false, based on whether parallel execution is desired, but mostly Jenkinsfile responsibility)
            tbi_parallel_execution: true
changelog:
    added:
        - Added example thing
    removed:
        - Removed example thing
    changed:
        - Changed example thing
    fixed:
        - Fixed example thing
authors:
    - Imre Tabur <imre.tabur@mail.ee>
```
