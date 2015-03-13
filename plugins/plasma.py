from os import system
from PyKDE4.kdecore import KConfig
from core.action import register_action, check_binary
from core import kdeapp

@check_binary("plasma-desktop")
@register_action
def theme(theme_name):
    """Set Plasma's theme to the theme provided."""
    config = KConfig("plasmarc")
    group = config.group('Theme')
    group.writeEntry('name', theme_name)
    config.sync()
    reload()

@check_binary("plasma-desktop")
@register_action
def reload():
    """Reload plasma's configuration."""
    kdeapp.restart('org.kde.krunner', 'krunner')
    if kdeapp.running_dbus('org.kde.plasma-desktop'):
        p = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
        p.reparseConfiguration()
        return True
    return False

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
        reload()
        return True
    return False
