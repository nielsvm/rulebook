from inspect import getargspec
from core import exit
import core.action, core.path

class Rule():
    """
    A rule object has a callable action, arguments and potential subrules.
    """

    def __init__(self, payload):
        """Initialize the rule object."""
        self.id = ""
        self.callable = None
        self.arguments = {}
        self.rules = []

        # Parse and extract the action from the first dictionary key.
        self.id = list(payload)[0]
        if not core.action.has(self.id):
            exit("Rule action '%s' does not exist!" % self.id)
        self.callable = core.action.get(self.id)

        # Build the arguments dictionary and register subrules.
        action_args = getargspec(self.callable)[0]
        if isinstance(payload[self.id], str):
            if 'path' in action_args[0]:
                self.arguments[action_args[0]] = core.path.rewrite(payload[self.id])
            else:
                self.arguments[action_args[0]] = payload[self.id]
        elif isinstance(payload[self.id], list):
            pos = 0
            for item in payload[self.id]:
                if isinstance(item, str):
                    if 'path' in action_args[pos]:
                        self.arguments[action_args[pos]] = core.path.rewrite(item)
                    else:
                        self.arguments[action_args[pos]] = item
                    pos = pos+1
                elif isinstance(item, dict):
                    self.rules.append(Rule(item))
                else:
                    exit("%s: parse error - unexpected format!" % self.id)
        if len(action_args) != len(self.arguments):
            if isinstance(self.callable.__defaults__, tuple):
                for default in self.callable.__defaults__:
                    self.arguments[action_args[len(self.arguments)]] = default
        if len(action_args) != len(self.arguments):
            exit("Action '%s' needs %d arguments, %d given " % (self.id, len(action_args), len(self.arguments)))

    def execute(self):
        """Execute the rule and its subrules if the main rule succeeded."""
        result = self.callable(**self.arguments)
        if len(self.rules) and (result == True):
            for rule in self.rules:
                rule.execute()
