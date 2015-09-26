from core.action import Action
from core import kdeapp

class DefaultProfile(Action):
    """Restart Konsole, open terminal instances will get killed."""

    def binary_dependencies(self):
        return ['konsole']

    def execute(self):
        return kdeapp.restart('org.kde.konsole', 'konsole')
