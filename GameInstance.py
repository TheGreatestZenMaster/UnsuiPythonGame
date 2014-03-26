'''
This class defines the object which holds all game information. 
Think of it like a giant game container in which everything goes.
'''

from items.Key import Key
from items.Door import Door
from rooms.Room import Room
from rooms.Hall import Hall
from Player.Player import Player
from monsters.Wolf import Wolf
from config import UnsuiConfigLoader


class GameInstance(object):
    def __init__(self):

        self.keys = [Key("Key", "Room 1", 10001),
                        Key("Key", "Room 2", 20002),
                        Key("Key", "Room 3", 30003)]

        self.rooms = [Room("Room 1", 1, False),
                         Room("Room 2", 2, False),
                         Room("Room 3", 3, False),
                         Room("Room 4", 4, False)]

        self.doors = [Door("Door 1", 1, False, None),
                         Door("Door 2", 2, True, 10001),
                         Door("Door 3", 3, True, 20002),
                         Door("Door 4", 4, True, 30003)]

        self.monsters = [Wolf("wolf", "Room 2"),
                            Wolf("wolf", "Room 3"),
                            Wolf("wolf", "Room 4")]

        self.player = Player("NoName", "Male", "Human", None)

        self.config_loader = UnsuiConfigLoader()
        self.config_loader.generate()