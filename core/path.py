from core import exit
from os.path import expanduser, exists

prefixes = {}

def add(variable, value):
    """Adds a variable and its substitute value to the registry."""
    prefixes[variable] = value

def register_path_prefix(f):
    """Registers a path prefix and its value replacement."""
    add("$%s" % f.__name__, f())

def rewrite(path):
    """Rewrites the given path and substitutes all registered prefixes."""
    for var, paths in prefixes.items():
        if var in path:
            if isinstance(paths, str):
                if exists(path.replace(var, paths)):
                    return path.replace(var, paths)
                else:
                    exit("UNABLE TO FIND '%s'!" % path.replace(var, paths))
            elif isinstance(paths, list):
                for _path in paths:
                    if exists(path.replace(var, _path)):
                        return path.replace(var, _path)
                exit("UNABLE TO FIND '%s' IN:\n - %s" % (path, "\n - ".join(paths)))
    return path

def user(path = None):
    """Get the absolute path relative from the users home directory."""
    if path:
        return "%s/%s" % (expanduser("~"), path)
    else:
        return expanduser("~")
