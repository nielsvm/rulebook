# import yaml
# from os.path import isfile
#
# from core import path, profile, application
# #
# # DEPRECATED?!
# #
#
# class Profiles():
#     """
#     The profiles object holds all profiles and makes them actionable.
#     """
#
#     def __init__(self, ymlfile):
#         """Initialize the profiles object by parsing the yml file given."""
#         self.statefile = None
#         self.profiles = []
#         self.current = 0
#
#         # Load the current profile if its set in the statefile.
#         self.statefile = path.user('.%s.current' % application.NAME)
#         if isfile(self.statefile):
#             with open(self.statefile, 'r') as state:
#                 self.current = int(state.read())
#                 state.close()
#         # Parse ymlfile and transform everything into objects.
#         try:
#             profiles = yaml.load(open(ymlfile, 'r'))
#         except Exception as e:
#             exit(e)
#         for id, _profile in profiles.items():
#             self.profiles.append(profile.Profile(id, _profile))
#
#     def get(self):
#         """Retrieve the currently active profile object."""
#         return self.profiles[self.current]
#
#     def next(self):
#         """Cycle the current profile to the next one."""
#         self.current = (self.current + 1) % len(self.profiles)
#         self.get().activate()
#         with open(self.statefile, 'w') as state:
#             state.write("%d" % self.current)
#             state.close()
