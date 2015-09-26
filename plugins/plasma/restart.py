from core.kdeaction import KDEAction
from core import kde

class Restart(KDEAction):
    """Restart Plasma."""

    def binary_dependencies4(self):
        return ['plasma-desktop']

    def execute4(self):
        return kde.restart('org.kde.plasma-desktop', 'plasma-desktop')

    def binary_dependencies5(self):
        return ['plasmashell']

    def execute5(self):
        return kde.restart('org.kde.plasmashell', 'plasmashell')
