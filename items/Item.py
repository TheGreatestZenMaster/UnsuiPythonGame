from Player.Inventory import Inventory
class Item(object):
	"""Base item class"""
	def __init__(self, id, name, description, contents=False):
		self.id = id
		self.name = name
		self.description = description

		if contents != False:
			self.inventory = Inventory()
        	for item in contents: self.inventory.add_item(item)

	
	# Base methods
	# These can be overridden in more complex items.

	def look(self):
		print self.description

	def look_in(self):
		if self.inventory:
			print self.inventory.list_of_items()