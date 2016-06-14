from core.action import Action
from subprocess import call
from time import sleep

class RunScript(Action):
    """Execute external commands."""

    def arguments(self):
        return [
            ('path', 'The full path (with arguments) to the external command.')
        ]

    def execute(self, path):
        call(path, shell=True)
        sleep(1)
        return True
