from os import system
from PyKDE4.kdecore import KConfig
from PyKDE4.kdeui import KGlobalSettings
from core.action import register_rule_action
from core.path import rewrite
from core import kdeapp

@register_rule_action
def colorscheme(scheme_path):
    """Change KDE's global color scheme to the provided scheme."""
    scheme = KConfig(rewrite(scheme_path))
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
    kdeapp.restart('org.kde.plasma-desktop', 'plasma-desktop')
    kdeapp.restart('org.kde.krunner', 'krunner')
    return True

@register_rule_action
def wallpaper(wallpaper_path):
    """Set Plasma's wallpaper to the image provided."""
    tmpfile = '/tmp/plasmawallpaperscript.js'
    with open(tmpfile, 'w') as js:
        js.write("var wallpaper = '%s';\n" % rewrite(wallpaper_path))
        js.write("var activity = activities()[0];\n")
        js.write("activity.currentConfigGroup = new Array('Wallpaper', 'image');\n")
        js.write("activity.writeConfig('wallpaper', wallpaper);\n")
        js.write("activity.writeConfig('userswallpaper', wallpaper);\n")
        js.write("activity.reloadConfig();\n")
    if kdeapp.running_dbus('org.kde.plasma-desktop'):
        plasma = kdeapp.get_object('org.kde.plasma-desktop', '/App')
        plasma.loadScriptInInteractiveConsole(tmpfile)
        system('xdotool search --name "Shell Scripting Console" windowactivate key control+e control+w')
        return True
    return False
