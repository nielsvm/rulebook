__all__ = ['colorscheme', 'notify', 'widget_style']
from os import popen
from plugins.kde import *
from core import path, kde

@path.register_path_prefix
def KDEWALLPAPER():
    paths = []
    if kde.version() == '5':
        wallpaper = popen("kf5-config --path wallpaper")
        wallpaper = wallpaper.read().replace("\n", '').split(":")
        for path in wallpaper:
            paths.append(path.rstrip('/'))
    elif kde.version() == '4':
        wallpaper = popen("kde4-config --path wallpaper")
        wallpaper = wallpaper.read().replace("\n", '').split(":")
        for path in wallpaper:
            paths.append(path.rstrip('/'))
    return paths

@path.register_path_prefix
def KDEDATA():
    paths = []
    if kde.version() == '5':
        data = popen("kf5-config --path data")
        data = data.read().replace("\n", '').split(":")
        for path in data:
            paths.append(path.rstrip('/'))
    elif kde.version() == '4':
        data = popen("kde4-config --path data")
        data = data.read().replace("\n", '').split(":")
        for path in data:
            paths.append(path.rstrip('/'))
    return paths
