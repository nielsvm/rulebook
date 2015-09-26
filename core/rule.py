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
        argspec = self.action.arguments()
        if isinstance(payload[self.id], str):
            if argspec[0][0] == 'path':
                try:
                    self.arguments['path'] = path.rewrite(payload[self.id])
                except Exception as e:
                    raise RuleActionException(self.id, str(e))
            else:
                self.arguments[argspec[0][0]] = payload[self.id]
        elif isinstance(payload[self.id], list):
            pos = 0
            for item in payload[self.id]:
                if isinstance(item, str):
                    if argspec[pos][0] == 'path':
                        try:
                            self.arguments['path'] = path.rewrite(item)
                        except Exception as e:
                            raise RuleActionException(self.id, str(e))
                    else:
                        self.arguments[argspec[pos][0]] = item
                    pos = pos+1
                elif isinstance(item, dict):
                    self.rules.append(Rule(item))
                else:
                    raise RuleParseException("unexpected format '%s'" % self.id)
        if len(argspec) != len(self.arguments):
            for arg in argspec:
                if isinstance(arg[1], tuple):
                    self.arguments[arg[0]] = arg[1][1]
        if len(argspec) != len(self.arguments):
            raise RuleMissingArguments(self.id, len(argspec), len(self.arguments))

    def execute(self):
        """Execute the rule and its subrules if the main rule succeeded."""
        try:
            result = self.action.execute(**self.arguments)
        except Exception as e:
            raise RuleActionException(self.id, str(e))
        if len(self.rules) and (result == True):
            for rule in self.rules:
                rule.execute()
