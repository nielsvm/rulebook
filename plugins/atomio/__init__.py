__all__ = ['find_replace', 'config_find_replace']
from plugins.atomio import *
from core.path import register_path_prefix, user
@register_path_prefix
def ATOMDIR():
    return user('.atom')
