class FileResourceNotFound(Exception):
    def __init__(self, needle, haystack=None):
        if haystack is None:
            self.msg = "Unable to find: %s" % needle
        else:
            self.msg = "Unable to find: %s\n\nIn any of these locations:\n - %s" % (needle, "\n - ".join(haystack))
    def __str__(self):
        return self.msg

class MissingDependency(Exception):
    pass

class RuleActionException(Exception):
    """Base class for exceptions related to rule action loading and execution."""
    def __init__(self, id, msg):
        self.id = id
        self.msg = msg
    def __str__(self):
        return "While loading or executing rule action '%s':\n\n%s." % (self.id, self.msg)

class RuleParseException(RuleActionException):
    """Base class for exceptions related to rule parsing and loading."""
    def __str__(self):
        return "parse error: %s." % self.msg

class RuleActionsDoesNotExist(RuleParseException):
    def __init__(self, id):
        self.id = id
        self.msg = "Rule action '%s' does not exist!" % id

class RuleMissingArguments(RuleParseException):
    def __init__(self, id, needs, given):
        self.id = id
        self.msg = "Rule action '%s' needs %d arguments, %d given!" % (id, needs, given)
