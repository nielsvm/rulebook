import subprocess
from os import system, getenv
from time import sleep
import dbus, psutil
from core.action import has_dependency, Action
from core.exceptions import RuntimeException

VERSION = getenv('KDE_SESSION_VERSION')
def version():
    """Find out what version of KDE is running."""
    if VERSION == None:
        raise RuntimeException('KDE_SESSION_VERSION variable not found!')
    if VERSION == '4':
        return VERSION
    elif VERSION == '5':
        return VERSION
    else:
        raise RuntimeException("KDE version %s not supported, sorry." % VERSION)

class KDE4Action(Action):
    """
    Specific action base for KDE4 applications.
    """

    def should_action_register():
        """Refuses to register when KDE4 isn't running."""
        return version() == '4'

class KDE5Action(Action):
    """
    Specific action base for KF5 applications.
    """

    def should_action_register():
        """Refuses to register when KF5 isn't running."""
        return version() == '5'

def get_dbus_object(bus_name, path):
    """Short-hand for returning a D-BUS object on the session bus."""
    return dbus.SessionBus().get_object(bus_name, path)

def running(bus_name, binary):
    """Check if a D-Bus service is activated or if a binary is running."""
    if running_dbus(bus_name):
        return True
    else:
        return running_binary(binary)

def running_binary(binary):
    """Check if the named binary is running."""
    for p in psutil.process_iter():
        if p.name() == binary:
            return p
    return False

def running_dbus(bus_name):
    """Check if a D-Bus service is activated."""
    return bus_name in dbus.SessionBus().list_names()

def restart(bus_name, binary):
    """Restart a D-BUS connected QApplication."""
    if quit(bus_name, binary):
        start(bus_name, binary)
        return True
    return False

def start(bus_name, binary):
    """Start a D-BUS connected QApplication."""
    if not running(bus_name, binary):
        system(binary)
        sleep(1)
        if not running(bus_name, binary):
            raise Exception("Couldn't properly start %s" % binary)
        return True
    return False

def quit(bus_name, binary):
    """Quit a D-BUS connected QApplication or application binary."""
    if running_dbus(bus_name):
        remote = dbus.SessionBus().get_object(bus_name, '/MainApplication')
        remote.quit()
        sleep(0.5)
        if running_dbus(bus_name):
            raise Exception("Couldn't properly quit %s" % bus_name)
        return True
    if running_binary(binary):
        running_binary(binary).terminate()
        if running_binary(binary):
            quit(bus_name, binary)
        return True
    return False

def writeconfig(group, key, value, file = None, type ='string'):
    """Write KConfig entries transparently across KDE4/5."""
    kdeversion = version()
    args = []
    if file:
        args.append('--file %s' % file)
    args.append('--group %s' % group)
    args.append('--key %s' % key)
    args.append('--type %s' % type)
    args.append(value)
    args = ' '.join(args)
    if kdeversion == 4:
        cmd = 'kwriteconfig'
    elif kdeversion:
        cmd = 'kwriteconfig5'
    if not has_dependency(cmd):
        raise RuntimeException('dependency %s not satisfied!' % cmd)
    opt = {'shell': True, 'stdout': subprocess.PIPE, 'stderr': subprocess.PIPE}
    call = subprocess.call("%s %s" % (cmd, args), **opt)
    if call != 0:
        raise RuntimeException("%s %s" % (cmd, args))
    return True
