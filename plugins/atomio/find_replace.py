from core.action import Action

class FindReplace(Action):
    """Rewrite a value in one of Atom's cson configuration files."""

    def binary_dependencies(self):
        return ['atom']

    def arguments(self):
        return [
            ('path', 'The configuration file to rewrite a value in.'),
            ('find', 'The string to be replaced.'),
            ('replace', 'The replacement value.')
        ]

    def execute(self, path, find, replace):
        new = []
        with open(path, 'r') as old:
            for line in old:
                new.append(line.replace(find, replace))
        with open(path, 'w') as pathnew:
            pathnew.write(''.join(new))
            pathnew.close()
        return True
