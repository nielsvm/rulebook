# from core.rule import Rule
# #
# # DEPRECATED?!
# #
# class Profile():
#     """
#     An object representing one profile with metadata and its rules.
#     """
#
#     def __init__(self, id, payload):
#         """Initialize the profile object and load its rules."""
#         self.id = id
#         self.title = payload["title"]
#         self.description = payload["description"]
#         self.rules = []
#         for rule in payload["rules"]:
#             self.rules.append(Rule(rule))
#
#     def activate(self):
#         """Activate this profile by executing all its rules."""
#         for rule in self.rules:
#             rule.execute()
