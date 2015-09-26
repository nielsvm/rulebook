from plugins.konsole.default_profile import DefaultProfile as DefaultProfileKonsole

class DefaultProfile(DefaultProfileKonsole):
    """Set Yakuakes's default Konsole profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies(self):
        return ['yakuake']

    def execute(self, path, binary = 'yakuake'):
        return DefaultProfileKonsole.execute(self, path, binary)
