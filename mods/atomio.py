
def replace(path, find, replace):
    """Rewrite a value in Atom's cson configuration files."""
    new = []
    with open(path, 'r') as old:
        for line in old:
            new.append(line.replace(find, replace))
    with open(path, 'w') as pathnew:
        pathnew.write(''.join(new))
        pathnew.close()
