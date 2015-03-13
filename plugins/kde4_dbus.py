from os import system
from time import sleep
import dbus, psutil

def get_object(bus_name, path):
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
