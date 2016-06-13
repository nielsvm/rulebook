from core import application, kde

class Notify4(kde.KDE4Action):
    """Send a desktop notification."""

    def arguments(self):
        return [
            ('text', 'The contents of the notification.'),
            ('title',
                (
                "The notification title, defaults to '%s'." % application.NAME,
                application.NAME))
        ]

    def execute(self, text, title):
        knotify = kde.get_dbus_object('org.kde.knotify', '/Notify')
        knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
        return True

class Notify5(kde.KDE5Action):
    """Send a desktop notification."""

    def arguments(self):
        return [
            ('text', 'The contents of the notification.'),
            ('title',
                (
                "The notification title, defaults to '%s'." % application.NAME,
                application.NAME))
        ]

    def execute(self, text, title):
        knotify = kde.get_dbus_object('org.kde.knotify', '/Notify')
        knotify.event("warning", "kde", [], title, text, [], [], 0, 0, dbus_interface="org.kde.KNotify")
        return True
