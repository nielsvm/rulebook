from core import path

def path_replace(path, find, replace):
    """Rewrite a value in one of Atom's cson configuration files."""
    new = []
    with open(path, 'r') as old:
        for line in old:
            new.append(line.replace(find, replace))
    with open(path, 'w') as pathnew:
        pathnew.write(''.join(new))
        pathnew.close()

def config(find, replace):
    """Rewrite a value in ~/.atom/config.cson."""
    path_replace(path.user('.atom/config.cson'), find, replace)
