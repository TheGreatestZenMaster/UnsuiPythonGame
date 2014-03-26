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
        
        
# NOTE: code below here is out-of-date and needs to be updated for use here. ~7yl4r

    # ------- Status Functions ------#
    # These functions are there to display the info about the room/player on request
    def visible_keys():
        dict_of_room_keys = generate_keys_dict()
        count = 0
        for key in dict_of_room_keys:
            if key.room == player.current_location:
                count += 1
        if count == 0:
            print "There are no keys"
        else:
            print "You can see %r keys." % count


    def visible_doors():
        if player.current_location == "Hallway":
            count = len(list_of_doors)
            print "You can see %r doors numbered accordingly." % count
        else:
            print "You can see the door you came through"


    def door_status(door):
            if door.locked:
                print "Door number %r is locked!" % door.number
            elif not door.locked:
                print "Door number %r is unlocked!" % door.number


    def visible_monsters():
        dict_of_room_monsters = populate_room_monster_dict()
        for monster in dict_of_room_monsters:
            print "You can see a %r!" % monster.name
            
    
    def battle_engine(monster):
        while True:
            Wolf.attack(monster)
            Player.attack(player, monster)


    def opponent_engine():
        dict_of_room_monsters = populate_room_monster_dict()
        for monster in dict_of_room_monsters:
            battle_engine(monster)
        return False

