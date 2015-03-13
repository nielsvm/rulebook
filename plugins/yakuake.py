from core.action import register_action, check_binary
from plugins import konsole
from core import kdeapp

@check_binary("yakuake")
@register_action
def default_profile(profile_name):
    """Set Yakuake's default Konsole profile and restart it."""
    return konsole.default_profile(profile_name, 'yakuake')

@check_binary("yakuake")
@register_action
def restart():
    return kdeapp.restart('org.kde.yakuake', 'yakuake')
