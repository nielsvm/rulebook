from plugins.plasma.reload import Reload
from core import kde

class Theme(Reload):
    """Set Plasma's theme to the theme provided."""

    def arguments(self):
        return [
            ('theme_name', 'The name of the theme to switch to.'),
        ]

    def binary_dependencies4(self):
        return ['plasma-desktop']

    def execute4(self, theme_name):
        kde.writeconfig('Theme', 'name', theme_name, 'plasmarc')
        return self.reload()

    def binary_dependencies5(self):
        return ['plasmashell']
