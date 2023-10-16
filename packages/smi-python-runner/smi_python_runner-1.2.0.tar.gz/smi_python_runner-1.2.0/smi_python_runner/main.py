import sys

from smi_python_runner.modules.loader import load_module
from smi_python_runner.runner_application import main

if __name__ == "__main__":
    loaded_module = load_module("application", "register")
    sys.exit(main(sys.argv))
