from smi_python_commons.config.application import Application


class EmptyRunner:

    def __init__(self):
        self.name = "empty-runner"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        return 0
