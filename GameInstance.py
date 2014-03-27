'''
This class defines the object which holds all game information. 
Think of it like a giant game container in which everything goes.
'''

import sys

from items.Key import Key
from items.Door import Door
from rooms.Room import Room
from Player.Player import Player
from monsters.Wolf import Wolf
from config import UnsuiConfigLoader
import user_input

BASE_ACTIONS = ["look", "exit", "stats", "location", "help"] # these are the actions which should always be available.

class GameInstance(object):
    def __init__(self):
        self.actions_available = BASE_ACTIONS

        self.player = Player("NoName", "Male", "Human", None)

        self.config_loader = UnsuiConfigLoader()
        self.config_loader.generate()

    #------- Actions Functions --------#
    def take_action(self,action):
        """
        This function takes an action specified by a string
         and completes that action.
        """
        # NOTE: currently there is no check to ensure that each action is available
        # TODO: check to see if action is available before trying... like:
        # if action in self.actions_available:

        # === Base Actions: ===
        room_dict = self.generate_rooms_dict()
        if action == "exit":
            sys.exit()
        elif action == "look":
            raise NotImplementedError('action_main call needs to be fixed') #action_main()
        elif action == "enter":
            raise NotImplementedError('action_main call needs to be fixed') #action_main()
        elif action == "go":
            travel_location = raw_input("Which Room?")
            for room in room_dict:
                if room.name.lower() == travel_location.lower():
                    self.player.current_location = room.name
                    self.player.player_location()
                    break
        elif action == "stats":
            self.player.player_status()
            return True
        elif action == "help":
            user_input.help_info()
            return True
        elif action == "location":
            self.player.player_location()
            return True

        # === iteminteractions ===
        elif action == "grab":
            self.player.inventory.add_item(user_input.choose_object(self.keys))

        # === monster interactions
        elif action == "fight":
            opponent_engine()
            return True
        else:
            print "That's not a valid command!!!"

    def generate_rooms_dict():
        return game.config_loader.get_by_type('room')
        
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

