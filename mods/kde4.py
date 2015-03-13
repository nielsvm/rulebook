from PyKDE4.kdeui import KGlobalSettings
from PyKDE4.kdecore import KConfig
from tempfile import mkstemp
from shutil import move
import os, sys

from mods import kde4_dbus

def colorscheme(scheme):
    """Change KDE's global color scheme to the provided scheme."""
    scheme = KConfig(scheme)
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
    kde4_dbus.restart('org.kde.plasma-desktop', 'plasma-desktop')
    kde4_dbus.restart('org.kde.krunner', 'krunner')

def konsole(profile_name, binary = 'konsole'):
    """Set Konsole's default profile and restart it."""
    bus_name = "org.kde.%s" % binary
    needs_restart = kde4_dbus.quit(bus_name, binary)
    config = KConfig("%src" % binary)
    group = config.group('Desktop Entry')
    group.writeEntry('DefaultProfile', profile_name)
    config.sync()
    if needs_restart:
        kde4_dbus.start(bus_name, binary)
        return True
    return False

def yakuake(profile_name):
    """Set Yakuake's default Konsole profile and restart it."""
    return konsole(profile_name, 'yakuake')

def wallpaper(value):
    """Set Plasma's wallpaper to the image provided."""
    tmpfile = '/tmp/plasmawallpaperscript.js'
    with open(tmpfile, 'w') as js:
        js.write("var wallpaper = '%s';\n" % value)
        js.write("var activity = activities()[0];\n")
        js.write(
            "activity.currentConfigGroup = new Array('Wallpaper', 'image');\n")
        js.write("activity.writeConfig('wallpaper', wallpaper);\n")
        js.write("activity.writeConfig('userswallpaper', wallpaper);\n")
        js.write("activity.reloadConfig();\n")
    if kde4_dbus.running_dbus('org.kde.plasma-desktop'):
        plasma = kde4_dbus.get_object('org.kde.plasma-desktop', '/App')
        plasma.loadScriptInInteractiveConsole(tmpfile)
        os.system('xdotool search --name "Shell Scripting Console" windowactivate key control+e control+w')
