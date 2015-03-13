from PyKDE4.kdecore import KConfig, KStandardDirs
from PyKDE4.kdeui import KGlobalSettings
from core.path import register_path_prefix, user
from core.action import register_action
from core import kdeapp, application

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

@register_action
def colorscheme(scheme_path):
    """Change KDE's global color scheme to the provided scheme."""
    scheme = KConfig(scheme_path)
    kdeglobals = KConfig('kdeglobals')
    for groupName in scheme.groupList():
        group = scheme.group(groupName)
        global_group = kdeglobals.group(groupName)
        for (k, v) in group.entryMap().items():
            global_group.writeEntry(k, v)
    kdeglobals.sync()
    KGlobalSettings.emitChange(KGlobalSettings.PaletteChanged)
    KGlobalSettings.emitChange(KGlobalSettings.StyleChanged)
    KGlobalSettings.emitChange(KGlobalSettings.SettingsChanged)
    if kdeapp.running_dbus('org.kde.plasma-desktop'):
        p = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
        p.reparseConfiguration()
    kdeapp.restart('org.kde.krunner', 'krunner')
    return True

@register_action
def notify(text, title = application.NAME):
    """Send a desktop notification."""
    knotify = kdeapp.get_dbus_object('org.kde.knotify', '/Notify')
    knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
    return True

@register_action
def widget_style(style_name):
    """Change KDE's widget style to the style given."""
    kdeglobals = KConfig("kdeglobals")
    group = kdeglobals.group('General')
    group.writeEntry('widgetStyle', style_name)
    kdeglobals.sync()
    KGlobalSettings.emitChange(KGlobalSettings.PaletteChanged)
    KGlobalSettings.emitChange(KGlobalSettings.StyleChanged)
    KGlobalSettings.emitChange(KGlobalSettings.SettingsChanged)
    if kdeapp.running_dbus('org.kde.plasma-desktop'):
        p = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
        p.reparseConfiguration()
    kdeapp.restart('org.kde.krunner', 'krunner')
    return True
