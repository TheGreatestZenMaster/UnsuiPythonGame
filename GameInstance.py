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
from parser import Parser

BASE_ACTIONS = ["look", "go", "location", "stats", "exit", "help"] # these are the actions which should always be available.


class GameInstance(object):
    def __init__(self):
        self.actions_available = BASE_ACTIONS

        self.player = Player("NoName", "Male", "Human", None)

        self.config_loader = UnsuiConfigLoader()
        self.config_loader.generate()

        self.parser = Parser()

    #------- Actions Functions --------#
    def generate_rooms_dict(self):
        ''' this returns a list of all rooms in the area '''
        return self.config_loader.get_by_type('room')

    def take_action(self, command):
        #print [i.name for i in self.player.current_location.contents]
        if command.verb.name == 'exit':
            sys.exit()
        if command.verb.name == 'look':
            if command.object != None:
                self.config_loader.get_by_type_and_name('item', command.object.name).look()
            else:
                print self.player.current_location.description


    """    
    def take_action(self,action,input=user_input.default_input):
        
        This function takes an action specified by a string
         and completes that action.
        
        # NOTE: currently there is no check to ensure that each action is available
        # TODO: check to see if action is available before trying... like:
        # if action in self.actions_available:
        # ^^^ Wouldn't this add additional proccessing cycles(a.k.a a for loop) to do the same thing? (~Joshua)

        # === Base Actions: ===
        room_dict = self.generate_rooms_dict()
        if action == "exit":
            sys.exit()
        elif action == "look":
            print self.player.current_location.description
        elif action == "enter":
            raise NotImplementedError('action_main call needs to be fixed') #action_main()
        elif action == "go":
            print self.player.current_location.exits
            travel_location = input("Which Room?")
            try:
                self.player.current_location = self.config_loader.get_by_type_and_name('room', self.player.current_location.exits[int(travel_location)-1])
            except ValueError:
                try:
                    self.player.current_location = self.config_loader.get_by_type_and_name('room', travel_location)
                except ValueError:
                    print 'Place not recognized.'
        elif action == "stats":
            self.player.player_status()

        elif action == "help":
            user_input.help_info()

        elif action == "location":
            self.player.player_location()

        # === iteminteractions ===
        elif action == "grab":
            raise NotImplementedError('grabbing items hasn\'t been implemented yet.')

        # === monster interactions
        elif action == "fight":
            raise NotImplementedError('combat engine hasn\'t been implemented yet.')
        else:
            print "That's not a valid command!!!"
    """