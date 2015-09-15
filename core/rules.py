from core.rule import Rule
from plugins import *

class Rules():
    """
    A collection of one or more rules.
    """

    def __init__(self, payload):
        """Parses a python list with dictionaries describing each rule."""
        self.rules = []
        for rule in payload:
            self.rules.append(Rule(rule))

    def execute(self):
        """Execute the rules and its subrules in order."""
        for rule in self.rules:
            rule.execute()
