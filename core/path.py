from os.path import expanduser, exists
from core.exceptions import FileResourceNotFound
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
                    raise FileResourceNotFound(path.replace(var, paths))
            elif isinstance(paths, list):
                for _path in paths:
                    if exists(path.replace(var, _path)):
                        return path.replace(var, _path)
                raise FileResourceNotFound(path, paths)
    return path

def user(path = None):
    """Get the absolute path relative from the users home directory."""
    if path:
        return "%s/%s" % (expanduser("~"), path)
    else:
        return expanduser("~")
