import sys, os.path, yaml
from core import exit, lock, rules

def exec_from_input():
    """Parse and execute incoming rules via file or stdin."""
    f = None
    if not sys.stdin.isatty():
        f = sys.stdin
    elif ((len(sys.argv) == 2) and os.path.isfile(sys.argv[1])):
        f = open(sys.argv[1])
    if f is not None:
        p = Parser(f)
        p.parse()
        if lock.acquire():
            p.execute()
            lock.release()
        else:
            exit("Another process seems to be running!")

class Parser():
    """
    JSON-based rules parser and executor.
    """

    def __init__(self, input):
        """Initialize the parser and store input."""
        self.rules = None
        self.input = input

    def parse(self):
        """Parse the input and raise syntax errors if they occur."""
        try:
            self.rules = rules.Rules(yaml.load(self.input))
        except Exception as e:
            print("\n=========================================================")
            print("  ERROR OCCURED DURING RULES LOADING, ABORTED")
            print("=========================================================\n")
            print("%s\n" % e)
            sys.exit()

    def execute(self):
        """Execute the rules in order"""
        self.rules.execute()
