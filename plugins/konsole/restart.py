from core import kde

class Restart4(kde.KDE4Action):
    """Restart Konsole, open terminal instances will get killed."""

    def binary_dependencies(self):
        return ['konsole']

    def execute(self):
        return kde.restart('org.kde.konsole', 'konsole')

class Restart5(kde.KDE5Action):
    """Restart Konsole, open terminal instances will get killed."""

    def binary_dependencies(self):
        return ['konsole']

    def execute(self):
        return kde.restart('org.kde.konsole', 'konsole')
