from core import kde
from subprocess import call

class WidgetStyle4(kde.KDE4Action):
    """Change KDE's widget style to the style given."""

    def arguments(self):
        return [
            ('style_name', 'The name of the style, e.g. "oxygen".')
        ]

    def binary_dependencies(self):
        return ['plasma-desktop', 'krunner']

    def execute(self, style_name):
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

class WidgetStyle5(kde.KDE5Action):
    """Change KDE's widget style to the style given."""

    def arguments(self):
        return [
            ('style_name', 'The name of the style, e.g. "oxygen".')
        ]

    def binary_dependencies(self):
        return ['plasmashell', 'krunner']

    def execute(self, style_name):
        kde.writeconfig("General", "widgetStyle", style_name, 'kdeglobals')
        kde.writeconfig("KDE", "widgetStyle", style_name, 'kdeglobals')
        call("dbus-send --session --type=signal /KGlobalSettings org.kde.KGlobalSettings.notifyChange int32:2 int32:0", shell=True)
        call("dbus-send --session --type=signal /KWin org.kde.KWin.reloadConfig", shell=True)
        return True
