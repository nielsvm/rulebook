from core.action import Action
from core import kdeapp

class Restart(Action):
    """Restart Plasma."""

    def binary_dependencies(self):
        return ['plasma-desktop']

    def execute(self):
        return kdeapp.restart('org.kde.plasma-desktop', 'plasma-desktop')
