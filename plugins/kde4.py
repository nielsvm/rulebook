from core.path import register_path_prefix, user


@register_path_prefix
def KDEDIR():
    return user('.kde')
