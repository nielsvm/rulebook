import configparser
from subprocess import call
from core import kde
from core.action import has_dependency

class ColorScheme4(kde.KDE4Action):
    """Change KDE's global color scheme to the provided scheme."""

    def arguments(self):
        return [
            ('scheme_path', 'The path to a .colors scheme file.')
        ]

    def binary_dependencies(self):
        return ['plasma-desktop', 'krunner']

    def execute(self, scheme_path):
        config = configparser.RawConfigParser()
        config.optionxform = str
        config.read(scheme_path)
        for group in config.sections():
            for key in config[group]:
                kde.writeconfig5(group, key, config[group][key], 'kdeglobals')
                kde.writeconfig4(group, key, config[group][key], 'kdeglobals')
        call("dbus-send --session --type=signal /KGlobalSettings org.kde.KGlobalSettings.notifyChange int32:0 int32:0", shell=True)
        call("dbus-send --session --type=signal /KWin org.kde.KWin.reloadConfig", shell=True)
        if kde.running_dbus('org.kde.plasma-desktop'):
            p = kde.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
            p.reparseConfiguration()
        kde.restart('org.kde.krunner', 'krunner')
        return True

class ColorScheme5(kde.KDE5Action):
    """Change KDE's global color scheme to the provided scheme."""

    def arguments(self):
        return [
            ('scheme_path', 'The path to a .colors scheme file.')
        ]

    def binary_dependencies(self):
        return ['plasmashell', 'krunner', 'dbus-send']

    def execute(self, scheme_path):
        config = configparser.RawConfigParser()
        config.optionxform = str
        config.read(scheme_path)
        for group in config.sections():
            for key in config[group]:
                if (has_dependency("kwriteconfig")):
                    kde.writeconfig4(group, key, config[group][key], 'kdeglobals')
                kde.writeconfig(group, key, config[group][key], 'kdeglobals')
        call("dbus-send --session --type=signal /KGlobalSettings org.kde.KGlobalSettings.notifyChange int32:0 int32:0", shell=True)
        call("dbus-send --session --type=signal /KWin org.kde.KWin.reloadConfig", shell=True)
        return True
