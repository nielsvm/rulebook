
#
# Replace a setting in Atom.io's config file.
#
def replaceAtomLine(path, find, replace):
  new = []
  with open(path, 'r') as old:
    for line in old:
      new.append(line.replace(find, replace))
  with open(path, 'w') as pathnew:
    pathnew.write(''.join(new))
    pathnew.close()
