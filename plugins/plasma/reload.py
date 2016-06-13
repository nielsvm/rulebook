from core import kde

class Reload4(kde.KDE4Action):
    """Reload plasma's configuration."""

    def binary_dependencies(self):
        return ['plasma-desktop', 'krunner']

    def reload(self):
        if kde.running_dbus('org.kde.plasma-desktop'):
            p = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
            p.reparseConfiguration()
            return True
        return False

    def execute(self):
        return self.reload()

class Reload5(kde.KDE5Action):
    """Reload plasma's configuration."""

    def binary_dependencies(self):
        return ['plasmashell', 'krunner']

    def reload(self):
        return kde.restart('org.kde.plasmashell', 'plasmashell')

    def execute(self):
        return self.reload()
