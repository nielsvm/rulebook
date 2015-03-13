from PyKDE4.kdecore import KConfig
from core.action import register_action, check_binary
from core import kdeapp

@check_binary("konsole")
@register_action
def default_profile(profile_name, binary = 'konsole'):
    """Set Konsole's default profile and restart it."""
    bus_name = "org.kde.%s" % binary
    config = KConfig("%src" % binary)
    group = config.group('Desktop Entry')
    group.writeEntry('DefaultProfile', profile_name)
    config.sync()
    return True

@check_binary("konsole")
@register_action
def restart():
    return kdeapp.restart('org.kde.konsole', 'konsole')
