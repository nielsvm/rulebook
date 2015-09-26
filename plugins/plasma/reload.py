from core.action import Action
from core import kdeapp

class Reload(Action):
    """Reload plasma's configuration."""

    def binary_dependencies(self):
        return ['plasma-desktop']

    def reload(self):
        kdeapp.restart('org.kde.krunner', 'krunner')
        if kdeapp.running_dbus('org.kde.plasma-desktop'):
            p = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
            p.reparseConfiguration()
            return True
        return False

    def execute(self):
        return self.reload()
