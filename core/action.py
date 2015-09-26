import subprocess
from collections import OrderedDict
from core.exceptions import MissingDependency

REGISTRY = {}
def registry(add_cls=None):
    """Global registry of action classes."""
    if add_cls != None:
        REGISTRY[add_cls._id] = add_cls
    return REGISTRY

DEPENDENCIES = {}
def has_dependency(binary):
    """Global binary dependency checker and registry."""
    if binary in DEPENDENCIES:
        return DEPENDENCIES[binary]
    else:
        opt = {'shell': True, 'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE}
        DEPENDENCIES[binary] = subprocess.call("type %s" % binary, **opt) == 0
        return DEPENDENCIES[binary]

class Registrar(type):
    """
    Metaclass that registers actions at the global registry.
    """
    def __init__(cls, name, parents, attrs):
        if (len(parents)):
            cls._id = attrs['__module__'].replace('plugins.', '')
            cls._doc = attrs['__doc__']
            if cls._id not in registry():
                registry(cls)
        return type.__init__(cls, name, parents, attrs)

class Action(metaclass=Registrar):
    """
    Base action class.
    """
    _id = None
    _doc = ""

    def arguments(self):
        """A list with tuples describing the actions arguments."""
        return []

    def argumentsDict(self):
        return OrderedDict(self.arguments())

    def binary_dependencies(self):
        """Lists any binary commands depended upon."""
        return []

    def has_missing_dependencies(self):
        """Identifies any potentially missing dependencies."""
        missing = []
        for dependency in self.binary_dependencies():
            if not has_dependency(dependency):
                missing.append(dependency)
        return missing

    def execute(self):
        """Invoke the action with given the parameters."""
        raise Exception("Not implemented.")

from plugins import *
