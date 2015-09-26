from core.action import Action
from core import kdeapp

class DefaultProfile(Action):
    """Restart Yakuake, open terminal instances will get killed."""

    def binary_dependencies(self):
        return ['yakuake']

    def execute(self):
        return kdeapp.restart('org.kde.yakuake', 'yakuake')
