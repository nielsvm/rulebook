from core.action import Action
from core import kde

class Reload(Action):
    """Reload plasma's configuration."""

    def binary_dependencies4(self):
        return ['plasma-desktop', 'krunner']

    def binary_dependencies5(self):
        return ['plasmashell', 'krunner']

    def reload(self):
        version = kde.version()
        kde.restart('org.kde.krunner', 'krunner')
        if version == '4':
            if kde.running_dbus('org.kde.plasma-desktop'):
                p = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/MainApplication')
                p.reparseConfiguration()
                return True
            return False
        elif version == '5':
            return kde.restart('org.kde.plasmashell', 'plasmashell')

    def execute(self):
        return self.reload()
