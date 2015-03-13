from os.path import expanduser

def user(path = None):
    """Get the absolute path relative from the users home directory."""
    if path:
        return "%s/%s" % (expanduser("~"), path)
    else:
        return expanduser("~")
