#!/usr/bin/python2
import os

from mods import *



#
# Make it day
#
def day():
  #kde.wallpaper('/home/nvmourik/doc/pic/wallpaper/rotterdam/centraal.jpg')
  #kde.wallpaper('/home/nvmourik/doc/pic/wallpaper/Nature/lavender-field.jpg')
  kde.wallpaper('1498967_866539266745416_4122185541686443994_o.jpg')
  kde.scheme('/home/nvmourik/.kde/share/apps/color-schemes/SoftMetalColder.colors');
  # setYakuakeProfile('day.profile')
  # replaceAtomLine('/home/nvmourik/.atom/config.cson', 'one-dark-ui', 'atom-light-ui')
  # replaceAtomLine('/home/nvmourik/.atom/config.cson', 'solarized-dark-syntax', 'solarized-light-syntax')

#
# Make it night
#
def night():
  kde.wallpaper('/usr/share/wallpapers/Prato/')
  kde.scheme('/usr/share/kde4/apps/color-schemes/ObsidianCoast.colors');
  # setYakuakeProfile('night.profile')
  # replaceAtomLine('/home/nvmourik/.atom/config.cson', 'atom-light-ui', 'one-dark-ui')
  # replaceAtomLine('/home/nvmourik/.atom/config.cson', 'solarized-light-syntax', 'solarized-dark-syntax')

#
# MAIN
#
mode = 'day'
cfg = '/home/nvmourik/.dayornight'
if os.path.isfile(cfg):
  with open(cfg, 'r') as old:
    mode = old.read()
if mode == 'day':
  mode = 'night'
  night()
elif mode == 'night':
  mode = 'day'
  day()
with open(cfg, 'w') as new:
  new.write("%s" % mode)
