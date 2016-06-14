from subprocess import call
from core import kde
from core.action import has_dependency

class IconTheme4(kde.KDE4Action):
    """Change KDE's icon theme."""

    def arguments(self):
        return [
            ('theme', 'Icon theme name.')
        ]

    def execute(self, theme):
        kde.writeconfig("Icons", "Theme", theme, file = "kdeglobals")
        return True

class IconTheme5(kde.KDE5Action):
    """Change KDE's icon theme."""

    def arguments(self):
        return [
            ('theme', 'Icon theme name.')
        ]

    def execute(self, theme):
        if (has_dependency("kwriteconfig")):
            kde.writeconfig4("Icons", "Theme", theme, file = "kdeglobals")
        kde.writeconfig("Icons", "Theme", theme, file = "kdeglobals")
        for x in range(0, 5):
            call("dbus-send --session --type=signal /KIconLoader org.kde.KGlobalSettings.iconChanged int32:%d" % x, shell=True)
            call("dbus-send --session --type=signal /KGlobalSettings org.kde.KGlobalSettings.notifyChange int32:4 int32:%d" % x, shell=True)
        call("dbus-send --session --type=signal /KWin org.kde.KWin.reloadConfig", shell=True)
        return True
