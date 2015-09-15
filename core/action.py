import subprocess
from core.exceptions import MissingDependency

registry = {}
blacklist = []

def check_binary(binary):
    """Checks if the binary the action requires is found."""
    opt = {'shell': True, 'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    def check_binary_decorator(f):
        if not subprocess.call("type %s" % binary, **opt) == 0:
            blacklist.append({'f': f, 'binary': binary})
        return f
    return check_binary_decorator

def register_action(f):
    """Registers functions that provide a callable rule action."""
    module = f.__module__.replace('plugins.', '')
    id = "%s.%s" % (module, f.__name__)
    registry[id] = f
    return f

def get(id):
    """Retrieves the action from the registry."""
    if has(id):
        return registry[id]
    return None

def has(id):
    """Checks if the id exists in the action registry."""
    if id in registry:
        for action in blacklist:
            if registry[id] == action['f']:
                raise MissingDependency("dependency '%s' not found!" % action['binary'])
        return True
    return False
