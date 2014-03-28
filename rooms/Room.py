'''
This is the base class for room. Rooms types or specific room definitions should extend this class.
'''
#----- Base Python imports------#
import sys



class Room(object):
    def __init__(self, name, description, exits, contents):
        """
        NB. A list must be passed into exits
        """
        self.self = self
        self.name = name
        self.description = description
        self.exits = exits
        self.contents = contents

    def on_entering_room(self):
        print "You have entered the %s" % self.name

    def objects_in_room(self):
        if len(self.objects) > 0:
            for room_object in self.objects:
                print "There is %s" % room_object.name
        else:
            print "The room seems to be empty"
