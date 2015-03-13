from os.path import expanduser

prefixes = {}

def add(variable, value):
    """Adds a variable and its substitute value to the registry."""
    prefixes[variable] = value

def register_path_prefix(f):
    """Registers a path prefix and its value replacement."""
    add("$%s" % f.__name__, f())

def rewrite(path):
    """Rewrites the given path and substitutes all registered prefixes."""
    for var, prefix in prefixes.items():
        path = path.replace(var, prefix)
    return path

def user(path = None):
    """Get the absolute path relative from the users home directory."""
    if path:
        return "%s/%s" % (expanduser("~"), path)
    else:
        return expanduser("~")
