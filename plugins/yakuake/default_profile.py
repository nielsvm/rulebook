from plugins.konsole.default_profile import DefaultProfile4, DefaultProfile5

class YakuakeProfile4(DefaultProfile4):
    """Set Yakuakes's default Konsole profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies(self):
        return ['yakuake']

    def execute4(self, path, binary = 'yakuake'):
        return DefaultProfileKonsole.execute(self, path, binary)

class YakuakeProfile5(DefaultProfile5):
    """Set Yakuakes's default Konsole profile."""

    def arguments(self):
        return [
            ('path', 'The relative path to a Konsole .profile file.')
        ]

    def binary_dependencies(self):
        return ['yakuake']

    def execute(self, path, binary = 'yakuake'):
        return DefaultProfileKonsole.execute(self, path, binary)
