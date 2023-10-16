import importlib
import logging

log = logging.getLogger(__name__)


def load_module(module_name: str, function_name: str = None):
    try:
        loaded_module = importlib.import_module(module_name)
        if function_name is not None and hasattr(loaded_module, function_name):
            func = getattr(loaded_module, function_name)
            if callable(func):
                func()
        return loaded_module
    except ImportError as e:
        raise e
