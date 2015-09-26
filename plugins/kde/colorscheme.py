from core.kdeaction import KDEAction
from core import kde

class ColorScheme(KDEAction):
    """Change KDE's global color scheme to the provided scheme."""

    def arguments(self):
        return [
            ('scheme_path', 'The path to a .colors scheme file.')
        ]

    def binary_dependencies4(self):
        return ['plasma-desktop', 'krunner']

    def execute4(self, scheme_path):
        from PyKDE4.kdecore import KConfig
        from PyKDE4.kdeui import KGlobalSettings
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
        if kde.running_dbus('org.kde.plasma-desktop'):
            p = kde.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
            p.reparseConfiguration()
        kde.restart('org.kde.krunner', 'krunner')
        return True

    def binary_dependencies5(self):
        return ['plasmashell', 'krunner']
