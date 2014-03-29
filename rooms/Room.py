'''
This is the base class for room. Rooms types or specific room definitions should extend this class.
'''
#----- Base Python imports------#
import sys
from Player.Inventory import Inventory

class Room(object):
    def __init__(self, name, description, exits, contents):
        """
        NB. A list must be passed into exits
        """
        self.self = self
        self.name = name
        self.description = description
        self.exits = exits

        self.inventory = Inventory()
        for item in contents:
            self.inventory.add_item(item)


    def on_entering_room(self):
        print "You have entered the %s" % self.name

    def objects_in_room(self):
        print self.inventory.list_of_items()
