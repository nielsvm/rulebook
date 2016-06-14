from core import kde

class DefaultProfile4(kde.KDE4Action):
    """Set Konsole's default profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies(self):
        return ['konsole']

    def execute(self, path, binary = 'konsole'):
        kde.writeconfig('Desktop Entry', 'DefaultProfile',
            path, "%src" % binary)
        return True

class DefaultProfile5(kde.KDE5Action):
    """Set Konsole's default profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies(self):
        return ['konsole']

    def execute(self, path, binary = 'konsole'):
        kde.writeconfig('Desktop Entry', 'DefaultProfile',
            path, "%src" % binary)
        return True
