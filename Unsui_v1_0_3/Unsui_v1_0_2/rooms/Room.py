'''
This is the base class for room. Rooms types or specific room definitions should extend this class.
'''
#----- Base Python imports------#
import sys



class Room(object):
    def __init__(self, number, name, victory):
        self.self = self
        self.number = number
        self.name = name
        self.victory = victory
