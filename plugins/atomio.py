from core.action import register_rule_action
from core.path import user, rewrite, register_path_prefix

@register_path_prefix
def ATOMDIR():
    return user('.atom')

@register_rule_action
def path_replace(path, find, replace):
    """Rewrite a value in one of Atom's cson configuration files."""
    path = rewrite(path)
    new = []
    with open(path, 'r') as old:
        for line in old:
            new.append(line.replace(find, replace))
    with open(path, 'w') as pathnew:
        pathnew.write(''.join(new))
        pathnew.close()
    return True

@register_rule_action
def config(find, replace):
    """Rewrite a value in ~/.atom/config.cson."""
    return path_replace('$ATOMDIR/config.cson', find, replace)
