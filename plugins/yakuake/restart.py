from core.kdeaction import KDEAction
from core import kde

class DefaultProfile(KDEAction):
    """Restart Yakuake, open terminal instances will get killed."""

    def binary_dependencies4(self):
        return ['yakuake']

    def execute4(self):
        return kde.restart('org.kde.yakuake', 'yakuake')
