from core import kde

class ColorScheme4(kde.KDE4Action):
    """Change KDE's global color scheme to the provided scheme."""

    def arguments(self):
        return [
            ('scheme_path', 'The path to a .colors scheme file.')
        ]

    def binary_dependencies(self):
        return ['plasma-desktop', 'krunner']

    def execute(self, scheme_path):
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

class ColorScheme5(kde.KDE5Action):
    """Change KDE's global color scheme to the provided scheme."""

    def arguments(self):
        return [
            ('scheme_path', 'The path to a .colors scheme file.')
        ]

    def binary_dependencies(self):
        return ['plasmashell', 'krunner']
