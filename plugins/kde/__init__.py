__all__ = ['colorscheme', 'notify', 'widget_style']
from os import popen
from plugins.kde import *
from core.action import has_dependency
from core.path import register_path_prefix, user
from core import kde

@register_path_prefix
def KDEWALLPAPER():
    paths = []
    if has_dependency("kf5-config"):
        wallpaper = popen("kf5-config --path wallpaper")
        for path in wallpaper.read().split(":"):
            paths.append(path.rstrip('/'))
    elif has_dependency("kde4-config"):
        wallpaper = popen("kde4-config --path wallpaper")
        for path in wallpaper.read().split(":"):
            paths.append(path.rstrip('/'))
    return paths

@register_path_prefix
def KDEDATA():
    paths = []
    if has_dependency("kf5-config"):
        data = popen("kf5-config --path data")
        for path in data.read().split(":"):
            paths.append(path.rstrip('/'))
    elif has_dependency("kde4-config"):
        data = popen("kde4-config --path data")
        for path in data.read().split(":"):
            paths.append(path.rstrip('/'))
    return paths
