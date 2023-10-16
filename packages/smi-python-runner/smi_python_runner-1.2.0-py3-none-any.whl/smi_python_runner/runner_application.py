import logging

import smi_python_commons.environment.variables
from smi_python_commons.arguments.argument import Argument
from smi_python_commons.arguments.config import Config
from smi_python_commons.arguments.constants import SMI_PROFILES_ARGUMENT, SMI_CONFIG_PATHS_ARGUMENT, \
    SMI_OPTIONAL_CONFIG_FILES_ARGUMENT
from smi_python_commons.config.application import Application

from smi_python_runner.logging.setup import logging_setup
from smi_python_runner.modules.loader import load_module
from smi_python_runner.services.arguments_register_service import arguments_register_service
from smi_python_runner.services.runner_register_service import runner_register_service

log = logging.getLogger(__name__)


def main(argv):
    arguments_config = [
        SMI_PROFILES_ARGUMENT,
        SMI_CONFIG_PATHS_ARGUMENT,
        SMI_OPTIONAL_CONFIG_FILES_ARGUMENT,
        Argument('runner-command', 'r', str, 'Runner to be executed', True),
        Argument('sub-command', 's', str, 'TBI sub-command', True)
    ]
    arguments_config.extend(arguments_register_service.arguments)
    argv_config = Config('Runner', arguments_config)
    app = logging_setup(Application(argv, argv_config))
    trying_to_load_module_by_app(app)
    runner = runner_register_service.get_runner(app.arguments.runner_command)
    log.info("Profiles: " + str(app.profiles_list))
    log.info("Runner: " + app.arguments.runner_command)
    log.info("Sub-command: " + app.arguments.sub_command)
    return runner.execute(app, app.arguments.sub_command)


def trying_to_load_module_by_app(app: Application):
    module_name = get_module_name_from_app(app)
    log.info("Trying to load module: " + module_name)
    try:
        load_module(module_name, "init")
    except ImportError as e:
        log.warning(f"Couldn't load module: {module_name}")


def get_module_name_from_app(app: Application):
    return get_module_name(app.arguments.runner_command, app.arguments.sub_command)


def get_module_name(runner_command: str, sub_command: str):
    prefix = smi_python_commons.environment.variables.get_environment_variable("RUNNERS_PREFIX")
    if prefix is not None:
        prefix = prefix + "."
    else:
        prefix = ""
    return prefix + "runners." + runner_command + "_" + sub_command
