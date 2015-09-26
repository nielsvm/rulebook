from PyKDE4.kdecore import KConfig
from core.action import Action

class DefaultProfile(Action):
    """Set Konsole's default profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies(self):
        return ['konsole']

    def execute(self, path, binary = 'konsole'):
        bus_name = "org.kde.%s" % binary
        config = KConfig("%src" % binary)
        group = config.group('Desktop Entry')
        group.writeEntry('DefaultProfile', profile_name)
        config.sync()
        return True
