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

        
        
    #------- Room Populating function ----#
    def generate_rooms_dict():
        return game.config_loader.get_by_type('room')


    def generate_doors_dict():
        room_dict = generate_rooms_dict()
        dict_of_doors_in_room = {}
        return game.player.current_location.exits
        if game.player.current_location.name == "Hallway":
            for door in game.doors:
                dict_of_doors_in_room[door] = door.name
            return dict_of_doors_in_room
        else:
            room = game.player.current_location
            for i in room_dict:
                if i.name == room:
                    room_number = i.number
                    for door in list_of_doors:
                        if room_number == door.number:
                            door_name = door.name
                            dict_of_doors_in_room[door] = door_name
                            return dict_of_doors_in_room


    def generate_keys_dict():
        dict_of_keys = {}
        for key in game.keys:
            dict_of_keys[key] = key.name
        return dict_of_keys


    def generate_room_keys_dict():
        dict_of_keys = generate_keys_dict()
        dict_of_room_keys = {}
        for key in dict_of_keys:
            if key.room == player.current_location:
                dict_of_room_keys[key] = key.name
                return dict_of_room_keys


    def generate_monsters_dict():
        dict_of_monsters = {}
        for monster in list_of_monsters:
            dict_of_monsters[monster] = monster.name
        return dict_of_monsters


    def populate_room_monster_dict():
        dict_of_room_monsters = {}
        dict_of_monsters = generate_monsters_dict()
        for monster in dict_of_monsters:
            if monster.room == player.current_location:
                dict_of_room_monsters[monster] = monster.name
        return dict_of_room_monsters

    #-------- Player Functions --------#
    def xp_check():
        """Checks player xp and necessary xp and calls the level up function if applicable"""
        global player
        xp_needed = player.level * 10 + 15
        if player.xp >= xp_needed:
            player.level_up()
            player.xp -= xp_needed
            print "You have leveled up!"
        else:
            xp_needed = player.level * 10 + 15
            print "Not enough xp to level up!", "You need %r" % xp_needed, "You have %r" % player.xp


    def prompt_levelup():
        check_levelup = raw_input("Would you like to see if you leveled up?")
        if check_levelup == "yes":
            xp_check()

    #------- Actions Functions --------#
    def take_action(action):
        """
        This function takes the input of the engine for
        action and completes that action
        Note: This function is only accessible inside the room loop
        """
        room_dict = generate_rooms_dict()
        dict_of_room_keys = generate_room_keys_dict()
        if action == "grab":
            game.player.inventory.add_item(user_input.choose_object(game.keys))
        elif action == "leave":
            for i in room_dict:
                if i.name == game.player.current_location:
                    game.current_room = i
                    if not game.current_room.victory:
                        room_xp = 25
                        game.player.xp += room_xp
                        print "Congrats you beat this room!"
                        print "You earned %r xp!" % room_xp
                        print "You exit the room!"
                        prompt_levelup()
                        game.current_room.victory = True
                        game.player.current_location = "Hallway"
                        return False
                    else:
                        print "You exit the room!"
                        game.current_room.victory = True
                        game.player.current_location = "Hallway"
                        return False
        elif action == "stats":
            game.player.player_status()
            return True
        elif action == "help":
            user_input.help_info()
            return True
        elif action == "fight":
            opponent_engine()
            return True
        elif action == "doors":
            visible_doors()
            return True
        elif action == "location":
            player.player_location()
            return True
        return True

    #------ Main Loops ---------- #
    def hall_room_transition():

        print game.player.current_location.exits
        room_choice = raw_input("Which room would you like to enter?(please enter a number)")
        if not room_choice.isdigit():
            print "Nope, it's not a number you entered."

        game.player.move_room(game.config_loader.get_by_type_and_name('room', game.player.current_location.exits[int(room_choice)-1]))

        # Locked doors are to be reimplemented soon. For now I'm testing the configuration loader functionality
        """
        dict_of_doors = generate_doors_dict()
        room_dict = generate_rooms_dict()
        for i in dict_of_doors:
            if i.number == int(room_choice):
                door_choice = i
                door_number = i.number
                if door_choice.locked:
                    print "The door seems to be locked. Maybe you need to use a key!"
                    use_key = raw_input("Use a key? (yes or no)")
                    if use_key.lower() == "yes":
                        for x in game.player.inventory:
                            if x.match == door_choice.match:
                                door_choice.locked = False
                                print "You used the key!"
                                door_status(door_choice)
                                enter_through_door = raw_input("Enter the room?")
                                if enter_through_door == "yes":
                                    print "You entered the room!"
                                    for room in room_dict:
                                        if room.number == door_number:
                                            player.current_location = room.name
                                            break
                            else:
                                print "There are no matching keys in your inventory!"
                                break
                    elif use_key.lower() == "no":
                        print "OK, but the door is still locked!"
                elif not door_choice.locked:
                    print "You entered the room!"
                    for room in room_dict:
                        if room.number == door_number:
                            game.player.move_room(room)
        """

    def action_main():
        """This main function is the secondary loop that is operational while the player is in the room
        """
        while True:
            if game.player.current_location.name == "Hallway":
                hall_room_transition()
                break
            else:
                generate_room_keys_dict()
                game_engine()
                return False

