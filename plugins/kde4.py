from PyKDE4.kdecore import KStandardDirs
from core.path import register_path_prefix, user

@register_path_prefix
def KDEHOME():
    for path in KStandardDirs().resourceDirs('wallpaper'):
        if user() in path:
            return path.replace('/share/wallpapers/', '')
    return user('.kde')

@register_path_prefix
def KDEWALLPAPER():
    paths = []
    for path in KStandardDirs().resourceDirs('wallpaper'):
        paths.append(path.rstrip('/'))
    return paths

@register_path_prefix
def KDEDATA():
    paths = []
    for path in KStandardDirs().resourceDirs('data'):
        paths.append(path.rstrip('/'))
    return paths
