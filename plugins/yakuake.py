from core.action import register_rule_action
from plugins import konsole

@register_rule_action
def dfltprofile(profile_name):
    """Set Yakuake's default Konsole profile and restart it."""
    return konsole.dfltprofile(profile_name, 'yakuake')
