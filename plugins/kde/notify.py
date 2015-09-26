from core.action import Action
from core import application
from core import kdeapp

class Notify(Action):
    """Send a desktop notification."""

    def arguments(self):
        return [
            ('text', 'The contents of the notification.'),
            ('title', "The notification title, defaults to '%s'." % application.NAME)
        ]

    def execute(self, text, title = application.NAME):
        knotify = kdeapp.get_dbus_object('org.kde.knotify', '/Notify')
        knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
        return True
