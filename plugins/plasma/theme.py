from plugins.plasma.reload import Reload
from PyKDE4.kdecore import KConfig

class Theme(Reload):
    """Set Plasma's theme to the theme provided."""

    def arguments(self):
        return [
            ('theme_name', 'The name of the theme to switch to.'),
        ]

    def binary_dependencies(self):
        return ['plasma-desktop']

    def execute(self, theme_name):
        config = KConfig("plasmarc")
        group = config.group('Theme')
        group.writeEntry('name', theme_name)
        config.sync()
        return self.reload()
