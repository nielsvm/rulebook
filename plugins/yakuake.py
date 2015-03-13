from core.action import register_rule_action
from plugins import konsole
from core import kdeapp

@register_rule_action
def default_profile(profile_name):
    """Set Yakuake's default Konsole profile and restart it."""
    return konsole.default_profile(profile_name, 'yakuake')

@register_rule_action
def restart():
    return kdeapp.restart('org.kde.yakuake', 'yakuake')
