from core.kdeaction import KDEAction
from core import kde

class WidgetStyle(KDEAction):
    """Change KDE's widget style to the style given."""

    def arguments(self):
        return [
            ('style_name', 'The name of the style, e.g. "oxygen".')
        ]

    def binary_dependencies4(self):
        return ['plasma-desktop', 'krunner']

    def execute4(self, style_name):
        from PyKDE4.kdecore import KConfig
        from PyKDE4.kdeui import KGlobalSettings
        kdeglobals = KConfig("kdeglobals")
        group = kdeglobals.group('General')
        group.writeEntry('widgetStyle', style_name)
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
