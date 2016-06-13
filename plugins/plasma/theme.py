from plugins.plasma.reload import Reload4, Reload5

class Theme4(Reload4):
    """Set Plasma's theme to the theme provided."""

    def arguments(self):
        return [
            ('theme_name', 'The name of the theme to switch to.'),
        ]

    def binary_dependencies(self):
        return ['plasma-desktop']

    def execute(self, theme_name):
        kde.writeconfig('Theme', 'name', theme_name, 'plasmarc')
        return self.reload()

class Theme5(Reload5):
    """Set Plasma's theme to the theme provided."""

    def arguments(self):
        return [
            ('theme_name', 'The name of the theme to switch to.'),
        ]

    def binary_dependencies(self):
        return ['plasmashell']

    def execute(self, theme_name):
        kde.writeconfig('Theme', 'name', theme_name, 'plasmarc')
        return True
