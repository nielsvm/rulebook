__all__ = ['kde', 'konsole', 'run_script', 'yakuake', 'plasma', 'atomio']

from core.path import register_path_prefix, user
@register_path_prefix
def HOME():
    return user()
