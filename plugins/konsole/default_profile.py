from core.kdeaction import KDEAction
from core import kde

class DefaultProfile(KDEAction):
    """Set Konsole's default profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies4(self):
        return ['konsole']

    def execute4(self, path, binary = 'konsole'):
        kde.writeconfig('Desktop Entry', 'DefaultProfile',
            path, "%src" % binary)
        return True

    def binary_dependencies5(self):
        return ['konsole']

    def execute5(self, path, binary = 'konsole'):
        kde.writeconfig('Desktop Entry', 'DefaultProfile',
            path, "%src" % binary)
        return True
