action_registry = {}

def register_rule_action(f):
    """Registers functions that provide a callable rule action."""
    module = f.__module__.replace('plugins.', '')
    id = "%s.%s" % (module, f.__name__)
    add(id, f)
    return f

def add(id, f):
    """Adds a action callable function to the registry."""
    action_registry[id] = f

def get(id):
    """Retrieves the action from the registry."""
    if has(id):
        return action_registry[id]
    return None

def has(id):
    """Checks if the id exists in the action registry."""
    return id in action_registry
