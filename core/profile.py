from itertools import cycle, islice, dropwhile
from os.path import isfile
from core import path, lock

def load(profiles):
    """Cycles between all profile callables and calls the next one in line."""
    if lock.acquire():
        statefile = path.user('.toggle-desktop')
        profile = 0
        if isfile(statefile):
            with open(statefile, 'r') as old:
                profile = (int(old.read()) + 1) % len(profiles)
        profiles[profile]()
        with open(statefile, 'w') as new:
            new.write("%d" % profile)
        lock.release()
    else:
        print("Another process seems to be active!")
