from core.exceptions import RuntimeException
from core.action import Action
from core import kde

class KDEAction(Action):
    """
    Specific action base for KDE applications.
    """

    def binary_dependencies(self):
        version = kde.version()
        if version == '4':
            return self.binary_dependencies4()
        elif version == '5':
            return self.binary_dependencies5()
        else:
            return []

    def execute(self, **kwargs):
        version = kde.version()
        if version == '4':
            return self.execute4(**kwargs)
        elif version == '5':
            return self.execute5(**kwargs)
        else:
            raise RuntimeException("unsupported version.")

    def binary_dependencies4(self):
        """Lists any binary commands depended upon."""
        return []

    def execute4(self, **kwargs):
        raise Exception("KDE 4 support for this action not yet supported")

    def binary_dependencies5(self):
        """Lists any binary commands depended upon."""
        return []

    def execute5(self, **kwargs):
        raise Exception("KDE 5 support for this action not yet supported")
