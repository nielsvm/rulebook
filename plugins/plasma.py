from os import system
from PyKDE4.kdecore import KConfig
from PyKDE4.kdeui import KGlobalSettings
from core.action import register_action, check_binary
from core import kdeapp, application

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
    kdeapp.restart('org.kde.systemsettings', 'systemsettings')
    kdeapp.restart('org.kde.krunner', 'krunner')
    restart()
    return True

@register_action
def notify(text, title = application.NAME):
    """Send a desktop notification."""
    knotify = kdeapp.get_dbus_object('org.kde.knotify', '/Notify')
    knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
    return True

@check_binary("plasma-desktop")
@register_action
def restart():
    """Restart plasma."""
    return kdeapp.restart('org.kde.plasma-desktop', 'plasma-desktop')

@check_binary("xdotool")
@check_binary("plasma-desktop")
@register_action
def wallpaper(wallpaper_path):
    """Set Plasma's wallpaper to the image provided."""
    tmpfile = '/tmp/plasmawallpaperscript.js'
    if kdeapp.running_dbus('org.kde.plasma-desktop'):
        with open(tmpfile, 'w') as js:
            js.write("var wallpaper = '%s';\n" % wallpaper_path)
            js.write("var activity = activities()[0];\n")
            js.write("activity.currentConfigGroup = new Array('Wallpaper', 'image');\n")
            js.write("activity.writeConfig('wallpaper', wallpaper);\n")
            js.write("activity.writeConfig('userswallpaper', wallpaper);\n")
            js.write("activity.reloadConfig();\n")
        plasma = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/App')
        plasma.loadScriptInInteractiveConsole(tmpfile)
        system('xdotool search --name "Shell Scripting Console" windowactivate key control+e control+w')
        return True
    return False
