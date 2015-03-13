from os import system
from time import sleep
from core.action import register_action
from core.path import register_path_prefix, user

@register_path_prefix
def HOME():
    return user()

@register_action
def script(path):
    """Call an external executable."""
    system(path)
    sleep(1)
    return True
