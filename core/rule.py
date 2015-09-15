from inspect import getargspec
from core.exceptions import *
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
        try:
            has_action = core.action.has(self.id)
        except Exception as e:
            raise RuleActionException(self.id, str(e))
        if not has_action:
            raise RuleActionsDoesNotExist(self.id)
        self.callable = core.action.get(self.id)

        # Build the arguments dictionary and register subrules.
        action_args = getargspec(self.callable)[0]
        if isinstance(payload[self.id], str):
            if 'path' in action_args[0]:
                try:
                    self.arguments[action_args[0]] = core.path.rewrite(payload[self.id])
                except Exception as e:
                    raise RuleActionException(self.id, str(e))
            else:
                self.arguments[action_args[0]] = payload[self.id]
        elif isinstance(payload[self.id], list):
            pos = 0
            for item in payload[self.id]:
                if isinstance(item, str):
                    if 'path' in action_args[pos]:
                        try:
                            self.arguments[action_args[pos]] = core.path.rewrite(item)
                        except Exception as e:
                            raise RuleActionException(self.id, str(e))
                    else:
                        self.arguments[action_args[pos]] = item
                    pos = pos+1
                elif isinstance(item, dict):
                    self.rules.append(Rule(item))
                else:
                    raise RuleParseException("unexpected format '%s'" % self.id)
        if len(action_args) != len(self.arguments):
            if isinstance(self.callable.__defaults__, tuple):
                for default in self.callable.__defaults__:
                    self.arguments[action_args[len(self.arguments)]] = default
        if len(action_args) != len(self.arguments):
            raise RuleMissingArguments(self.id, len(action_args), len(self.arguments))

    def execute(self):
        """Execute the rule and its subrules if the main rule succeeded."""
        try:
            result = self.callable(**self.arguments)
        except Exception as e:
            raise RuleActionException(self.id, str(e))
        if len(self.rules) and (result == True):
            for rule in self.rules:
                rule.execute()
