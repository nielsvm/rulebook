import os

def exit(msg):
    """Exit the process with the given error messaging."""
    msg = str(msg)
    if "\n" in msg:
        os.sys.exit("ERROR:\n\n%s\n" % msg)
    else:
        os.sys.exit("ERROR: %s\n" % msg)
