from core.kdeaction import KDEAction
from core import kde

class DefaultProfile(KDEAction):
    """Restart Konsole, open terminal instances will get killed."""

    def binary_dependencies4(self):
        return ['konsole']

    def execute4(self):
        return kde.restart('org.kde.konsole', 'konsole')

    def binary_dependencies5(self):
        return ['konsole']

    def execute5(self):
        return kde.restart('org.kde.konsole', 'konsole')
