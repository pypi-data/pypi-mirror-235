from smi_python_commons.config.application import Application


class ApplicationBaseRunner:

    def __init__(self):
        self.name = "default"

    def get_name(self):
        return self.name

    def execute(self, app: Application, sub_command: str):
        return 0


DEFAULT_RUNNER = ApplicationBaseRunner()
