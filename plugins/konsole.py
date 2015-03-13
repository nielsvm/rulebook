from PyKDE4.kdecore import KConfig
from core.action import register_rule_action
from core import kdeapp

@register_rule_action
def dfltprofile(profile_name, binary = 'konsole'):
    """Set Konsole's default profile and restart it."""
    bus_name = "org.kde.%s" % binary
    needs_restart = kdeapp.quit(bus_name, binary)
    config = KConfig("%src" % binary)
    group = config.group('Desktop Entry')
    group.writeEntry('DefaultProfile', profile_name)
    config.sync()
    if needs_restart:
        kdeapp.start(bus_name, binary)
        return True
    return False
