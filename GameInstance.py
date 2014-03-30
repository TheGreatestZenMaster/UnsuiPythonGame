'''
This class defines the object which holds all game information. 
Think of it like a giant game container in which everything goes.
'''
import sys
from datetime import datetime

from items.Key import Key
from items.Door import Door
from rooms.Room import Room
from Player.Player import Player
from monsters.Wolf import Wolf
from config import UnsuiConfigLoader
import user_input
from input_parser import Parser
from make_events import getEventList

BASE_ACTIONS = ["look", "go", "location", "stats", "exit", "help"] # these are the actions which should always be available.


class GameInstance(object):
    def __init__(self):
        self.GAME_START = datetime.now()
        self.commands_entered = 0
        
        self.actions_available = BASE_ACTIONS

        self.player = Player("NoName", "Male", "Human", None)
        
        self.parser = Parser()

        self.config_loader = UnsuiConfigLoader()
        self.config_loader.generate()
        
        self.events = getEventList(self)

    #------- Actions Functions --------#
    def generate_rooms_dict(self):
        ''' this returns a list of all rooms in the area '''
        return self.config_loader.get_by_type('room')
        
    def check_events(self):
        '''
        Checks all events in the event list to see 
        if they have been triggered. If so, performs event action
        and removes event from the list.
        '''
        for event in self.events:
            if event.check():
                self.events.remove(event)

    def take_action(self, command, input=user_input.default_input):

        # This method now uses the Command object returned from the Parser
        # This means you can call commands with 2 words, e.g. 'look desk'

        # TODO:
        #   - Reimplement other archived commands.
        #   - Move this code to user_input maybe

        if command:
            if command.verb.name == 'exit':
                sys.exit()

            if command.verb.name == 'look':
                # call look function of object of command
                if command.object == None:
                    print self.player.current_location.description
                    
                elif command.object.type == 'error':
                    print "I don't understand %s" % command.object.name
                else:    # If there is no object of look it will print the current room's description
                    self.config_loader.get_by_type_and_name('item', command.object.name).look()

            if command.verb.name == 'go':
                if command.object != None:
                    try:
                        self.player.current_location = self.config_loader.get_by_type_and_name('room', command.object.name)
                    except ValueError as err:
                        if err.message[0:16] == 'Cannot find room':
                            print err.message
                        else:
                            raise
                else:
                    print self.player.current_location.exits
                    travel_location = input("Which Room?")
                    try:
                        self.player.current_location = self.config_loader.get_by_type_and_name('room', self.player.current_location.exits[int(travel_location)-1])
                    except ValueError:
                        try:
                            self.player.current_location = self.config_loader.get_by_type_and_name('room', travel_location)
                        except ValueError:
                            print 'Place not recognized.'
                            
            if command.verb.name == 'stats':
                self.player.player_status()
                print ' ### GAME STATS ### '
                print 'game started : ', self.GAME_START
                print 'commands entered : ', self.commands_entered

            if command.verb.name == 'help':
                user_input.help_info()

            if command.verb.name == 'location':
                self.player.player_location()

            if command.verb.name == 'inventory' or command.verb.name == 'bag':
                print self.player.inventory.list_of_items()

            self.commands_entered += 1
        else:
            print "Command not recognised."