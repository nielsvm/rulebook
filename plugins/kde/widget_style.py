from PyKDE4.kdecore import KConfig
from PyKDE4.kdeui import KGlobalSettings
from core.action import Action
from core import kdeapp

class WidgetStyle(Action):
    """Change KDE's widget style to the style given."""

    def arguments(self):
        return [
            ('style_name', 'The name of the style, e.g. "oxygen".')
        ]

    def execute(self, style_name):
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
