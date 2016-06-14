from plugins.plasma.reload import Reload4, Reload5
from core import kde, path
from os import system, popen

class Wallpaper4(Reload4):
    """Set Plasma's wallpaper to the image provided."""

    def arguments(self):
        return [
            ('wallpaper_path', 'Directory containing plasma wallpaper or a file path.'),
        ]

    def binary_dependencies(self):
        return ['plasma-desktop', 'xdotool']

    def execute(self, wallpaper_path):
        tmpfile = '/tmp/plasmawallpaperscript.js'
        if kde.running_dbus('org.kde.plasma-desktop'):
            with open(tmpfile, 'w') as js:
                js.write("var wallpaper = '%s';\n" % wallpaper_path)
                js.write("var activity = activities()[0];\n")
                js.write("activity.currentConfigGroup = new Array('Wallpaper', 'image');\n")
                js.write("activity.writeConfig('wallpaper', wallpaper);\n")
                js.write("activity.writeConfig('userswallpaper', wallpaper);\n")
                js.write("activity.reloadConfig();\n")
            plasma = kde.get_dbus_object('org.kde.plasma-desktop', '/App')
            plasma.loadScriptInInteractiveConsole(tmpfile)
            system('xdotool search --name "Shell Scripting Console" windowactivate key control+e control+w')
            self.reload()
            return True
        return False

class Wallpaper5(Reload5):
    """Set Plasma's wallpaper to the image provided."""

    def arguments(self):
        return [
            ('wallpaper_path', 'Directory containing plasma wallpaper or a file path.'),
        ]

    def binary_dependencies(self):
        return ['plasmashell', 'xdotool', 'kwin_x11']

    def execute(self, wallpaper_path):
        if kde.running_dbus('org.kde.plasmashell'):
            tmpfile = '/tmp/plasmawallpaperscript.js'
            js = """var activity = currentActivity();
                var desktops = desktopsForActivity(activity);
                for (var desktop in desktops) {
                  desktops[desktop].wallpaperPlugin = 'org.kde.image';
                  desktops[desktop].wallpaperMode = '';
                  desktops[desktop].currentConfigGroup = ['Wallpaper', 'org.kde.image', 'General'];
                  desktops[desktop].writeConfig('Image', wallpaper_path);
                }"""
            js = js.replace('  ', '').replace("\n", '  ')
            js = "wallpaper_path = 'file://%s';%s" % (wallpaper_path, js)
            # Now lets get hacky, load the script into the console and click buttons.
            plasma = kde.get_dbus_object('org.kde.plasmashell', '/PlasmaShell')
            plasma.showInteractiveConsole()
            mouse_x_y = popen("xdotool getmouselocation --shell")
            mouse_x_y = mouse_x_y.read().replace("\n", ' ').split(" ")
            mouse_x_y = "%s %s" % (mouse_x_y[0].replace("X=", ''), mouse_x_y[1].replace("Y=", ''))
            system('xdotool search --name "Shell Scripting Console" windowactivate')
            system('xdotool search --name "Shell Scripting Console" key control+a BackSpace')
            system('xdotool search --name "Shell Scripting Console" windowactivate type "%s"' % js)
            system('xdotool search --name "Shell Scripting Console" windowactivate mousemove --window %1 370 50 click 1 key control+w')
            system('xdotool mousemove %s' % mouse_x_y)
            return True
        return False
