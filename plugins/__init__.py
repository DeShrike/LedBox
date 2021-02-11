import importlib
from importlib import resources
from inspect import isclass, isabstract

#from menu import Menu
#from clock import Clock
#from snake import Snake

PLUGINS = []

def _import(package, plugin):
    """Import the given plugin file from a package"""
    module = importlib.import_module(f"{package}.{plugin}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if isclass(attribute) and not isabstract(attribute):
            print(f"Loaded Plugin {attribute}")
            PLUGINS.append(attribute)

def _import_all(package):
    files = resources.contents(package)
    plugins = [f[:-3] for f in files if f.endswith(".py") and f[0] != "_"]
    for plugin in plugins:
        _import(package, plugin)

_import_all(__package__)
