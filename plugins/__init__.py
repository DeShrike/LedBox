import importlib
import logging
from importlib import resources
from inspect import isclass, isabstract

PLUGINS = []
_logger = None

def _import(package, plugin):
    """Import the given plugin file from a package"""
    module = importlib.import_module(f"{package}.{plugin}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isclass(attribute) and not isabstract(attribute):
            _logger.debug(f"Loaded Plugin {attribute}")
            PLUGINS.append(attribute)

def _import_all(package):
    files = resources.contents(package)
    plugins = [f[:-3] for f in files if f.endswith(".py") and f[0] != "_"]
    for plugin in plugins:
        _import(package, plugin)

_logger = logging.getLogger(__name__)
_logger.info("Loading plugins")

_import_all(__package__)
