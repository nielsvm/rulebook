from core.path import rewrite
from plugins.atomio.find_replace import FindReplace

class ConfgFindReplace(FindReplace):
    """Rewrite a value in ~/.atom/config.cson."""

    def arguments(self):
        return [
            ('find', 'The string to be replaced.'),
            ('replace', 'The replacement value.')
        ]

    def execute(self, find, replace):
        return FindReplace.execute(self, rewrite('$ATOMDIR/config.cson'), find, replace)
