from os import unlink
from os.path import isfile
from core import path

def acquire():
    """Acquire a lock to execute the program."""
    lockfile = path.user('.toggle-desktop.lock')
    if isfile(lockfile):
        return False
    with open(lockfile, 'w') as lock:
        lock.write('Do not remove this file!')
        lock.close()
    return True

def release():
    """Release the lock once the program is finished."""
    lockfile = path.user('.toggle-desktop.lock')
    if isfile(lockfile):
        unlink(lockfile)
        return True
    return False
