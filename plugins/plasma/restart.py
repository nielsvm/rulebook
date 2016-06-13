from core import kde

class Restart4(kde.KDE4Action):
    """Restart Plasma."""

    def binary_dependencies(self):
        return ['plasma-desktop']

    def execute(self):
        return kde.restart('org.kde.plasma-desktop', 'plasma-desktop')

class Restart5(kde.KDE5Action):
    """Restart Plasma."""

    def binary_dependencies(self):
        return ['plasmashell']

    def execute(self):
        return kde.restart('org.kde.plasmashell', 'plasmashell')
