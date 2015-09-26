from core.action import Action
from os import system
from time import sleep

class RunScript(Action):
    """Execute external commands."""

    def arguments(self):
        return [
            ('path', 'The full path (with arguments) to the external command.')
        ]

    def execute(self, path):
        system(path)
        sleep(1)
        return True
