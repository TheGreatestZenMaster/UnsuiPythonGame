class Item(object):
	"""Base item class"""
	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

	
	# Base methods
	# These can be overridden in more complex items.

	def look(self):
		print self.description