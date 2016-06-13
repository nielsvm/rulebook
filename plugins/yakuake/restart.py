from core import kde

class Restart4(kde.KDE4Action):
    """Restart Yakuake, open terminal instances will get killed."""

    def binary_dependencies(self):
        return ['yakuake']

    def execute(self):
        return kde.restart('org.kde.yakuake', 'yakuake')

class Restart5(kde.KDE5Action):
    """Restart Yakuake, open terminal instances will get killed."""

    def binary_dependencies(self):
        return ['yakuake']

    def execute(self):
        return kde.restart('org.kde.yakuake', 'yakuake')
