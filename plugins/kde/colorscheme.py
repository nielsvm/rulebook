from PyKDE4.kdecore import KConfig
from PyKDE4.kdeui import KGlobalSettings
from core.action import Action
from core import kdeapp

class ColorScheme(Action):
    """Change KDE's global color scheme to the provided scheme."""

    def arguments(self):
        return [
            ('scheme_path', 'The path to a .colors scheme file.')
        ]

    def execute(self, scheme_path):
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
