from core.kdeaction import KDEAction
from core import application, kde

class Notify(KDEAction):
    """Send a desktop notification."""

    def arguments(self):
        return [
            ('text', 'The contents of the notification.'),
            ('title', "The notification title, defaults to '%s'." % application.NAME)
        ]

    def execute4(self, text, title = application.NAME):
        knotify = kde.get_dbus_object('org.kde.knotify', '/Notify')
        knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
        return True

    def execute5(self, text, title = application.NAME):
        knotify = kde.get_dbus_object('org.kde.knotify', '/Notify')
        knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
        return True
