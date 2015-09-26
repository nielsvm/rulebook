from plugins.plasma.reload import
from core import kdeapp

class Wallpaper(Reload):
    """Set Plasma's wallpaper to the image provided."""

    def arguments(self):
        return [
            ('wallpaper_path', 'Directory containing plasma wallpaper or a file path.'),
        ]

    def binary_dependencies(self):
        return ['plasma-desktop', 'xdotool']

    def execute(self, theme_name):
        tmpfile = '/tmp/plasmawallpaperscript.js'
        if kdeapp.running_dbus('org.kde.plasma-desktop'):
            with open(tmpfile, 'w') as js:
                js.write("var wallpaper = '%s';\n" % wallpaper_path)
                js.write("var activity = activities()[0];\n")
                js.write("activity.currentConfigGroup = new Array('Wallpaper', 'image');\n")
                js.write("activity.writeConfig('wallpaper', wallpaper);\n")
                js.write("activity.writeConfig('userswallpaper', wallpaper);\n")
                js.write("activity.reloadConfig();\n")
            plasma = kdeapp.get_dbus_object('org.kde.plasma-desktop', '/App')
            plasma.loadScriptInInteractiveConsole(tmpfile)
            system('xdotool search --name "Shell Scripting Console" windowactivate key control+e control+w')
            reload()
            return True
        return False
