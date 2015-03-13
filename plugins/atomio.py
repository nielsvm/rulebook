from core.action import register_action
from core.path import user, rewrite, register_path_prefix

@register_path_prefix
def ATOMDIR():
    return user('.atom')

@register_action
def find_replace(path, find, replace):
    """Rewrite a value in one of Atom's cson configuration files."""
    new = []
    with open(path, 'r') as old:
        for line in old:
            new.append(line.replace(find, replace))
    with open(path, 'w') as pathnew:
        pathnew.write(''.join(new))
        pathnew.close()
    return True

@register_action
def config_find_replace(find, replace):
    """Rewrite a value in ~/.atom/config.cson."""
    return find_replace(rewrite('$ATOMDIR/config.cson'), find, replace)
