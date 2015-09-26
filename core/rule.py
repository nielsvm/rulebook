from inspect import getargspec
from core.exceptions import *
from core import action, path

class Rule():
    """
    A rule object has a callable action, arguments and potential subrules.
    """

    def __init__(self, payload):
        """Initialize the rule object."""
        self.id = ""
        self.action = None
        self.arguments = {}
        self.rules = []

        # The first dict key is the action ID, verify and instantiate it.
        self.id = list(payload)[0]
        if not self.id in action.registry():
            raise RuleActionsDoesNotExist(self.id)
        try:
            self.action = action.registry()[self.id]()
        except Exception as e:
            raise RuleActionException(self.id, str(e))

        # Test for any missing dependencies and stop if anything is missing.
        missing = self.action.has_missing_dependencies()
        if len(missing):
            if len(missing) == 1:
                raise RuleActionException(self.id, "missing dependency %s" % missing[0])
            else:
                raise RuleActionException(self.id, "missing dependencies: %s" % ', '.join(missing))

        # Build the arguments dictionary and register any found subrules.
        action_args = getargspec(self.action.execute)[0]
        del action_args[0]
        if isinstance(payload[self.id], str):
            if 'path' in action_args[0]:
                try:
                    self.arguments[action_args[0]] = path.rewrite(payload[self.id])
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
                            self.arguments[action_args[pos]] = path.rewrite(item)
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
            if isinstance(self.action.execute.__defaults__, tuple):
                for default in self.action.execute.__defaults__:
                    self.arguments[action_args[len(self.arguments)]] = default
        if len(action_args) != len(self.arguments):
            raise RuleMissingArguments(self.id, len(action_args), len(self.arguments))

    def execute(self):
        """Execute the rule and its subrules if the main rule succeeded."""
        try:
            result = self.action.execute(**self.arguments)
        except Exception as e:
            raise RuleActionException(self.id, str(e))
        if len(self.rules) and (result == True):
            for rule in self.rules:
                rule.execute()
