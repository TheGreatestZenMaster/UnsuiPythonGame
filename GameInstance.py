'''
This class defines the object which holds all game information. 
Think of it like a giant game container in which everything goes.
'''
import sys
from datetime import datetime
import pickle

from Player.Player import Player
from config import UnsuiConfigLoader
import user_input
from input_parser import Parser
from gamedata.getEventList import getStartingEvents
from send_data import invalid_input
from lib.eventsEngine.EventsEngine import EventsEngine
from lib.colorama.colorama import Fore

BASE_ACTIONS = ["look", "go", "location", "stats", "exit", "help", "quests"] # these are the actions which should always be available.
DEFAULT_SAVE_FILE = 'unsui_default.save'

class GameInstance(object):
    def __init__(self, load=False, input_func=user_input.default_input):
        if load == False:
            # define attributes: #
            self.player = Player("NoName", "Male", "Human", None)           
            self.parser = Parser()
            self.config_loader = UnsuiConfigLoader()
            self.GAME_START = datetime.now()
            self.commands_entered = 0
            self.actions_available = BASE_ACTIONS
                        
            # call set up functions: #
            self.config_loader.generate()    
            user_input.opening_setup(self,input=input_func)
            self.events_engine = EventsEngine.EventsEngine(getStartingEvents(self))
        else:
            self.load_game(load)

    #------- Actions Functions --------#
    def generate_rooms_dict(self):
        ''' this returns a list of all rooms in the area '''
        return self.config_loader.get_by_type('room')
        
    def check_events(self):
        '''
        Checks all events in the event list to see 
        if they have been triggered.
        '''
        self.events_engine.checkEvents()
                
    def load_game(self,fname):
        with open(fname, 'rb') as f:
            newgame = pickle.load(f)
            self.set(newgame)
            del newgame
        # Deprecated, replaced by Pickle. Leave here.
        #self.config_loader.generate(load)
        #self.player = self.config_loader.create_player()
        
    def set(self,game):
        '''sets all attributes in this game equal to those of given game'''
        self.player = game.player
        self.parser = game.parser
        self.config_loader = game.config_loader
        self.GAME_START = game.GAME_START
        self.commands_entered = game.commands_entered
        self.actions_available = game.actions_available
        self.events = game.events

    def save_game(self,fname=DEFAULT_SAVE_FILE):
        with open(fname,'wb') as f:
            pickle.dump(self,f,pickle.HIGHEST_PROTOCOL)
        # Deprecated, replaced by Pickle. Leave here.
        #self.config_loader.save_game(self.player)
        
    def exit_game(self,save=True):
        if save==True:
            self.save_game()
        sys.exit()

    def take_action(self, command, input=user_input.default_input):

        # This method now uses the Command object returned from the Parser
        # This means you can call commands with 2 words, e.g. 'look desk'

        # TODO:
        #   - Move this code to user_input maybe
        #     ^ Any thoughts on this? This code will become very large as we implement more verbs.
        #       Unless we can devise a smart way to handle them all.

        if command:
            if command.verb.name == 'exit':
                self.exit_game()

            if command.verb.name == 'look':
                # call look function of object of command
                if command.object == None:
                    print self.player.current_location.description
                    
                elif command.object.type == 'error':
                    invalid_input("I don't understand %s" % command.object.name,
                        input_string=command.raw,
                        tag='unknown object error',
                        game=self)
                elif 'in' in command.object.prepositional_modifiers:

                    self.config_loader.get_by_type_and_name('item', command.object.name).look_in()

                else:    # If there is no object of look it will print the current room's description
                    self.config_loader.get_by_type_and_name('item', command.object.name).look()

            if command.verb.name == 'go':
                if command.object != None:
                    try:
                        target_room = self.config_loader.get_by_type_and_name('room', command.object.name)
                        if target_room.name in self.player.current_location.exits:
                            self.player.current_location = target_room
                        else:
                            print 'Cannot go to '+Fore.GREEN+"{}".format(target_room.name)
                    except ValueError as err:
                        if err.message[0:16] == 'Cannot find room':
                            invalid_input(err.message,
                                input_string=command.raw,
                                tag='room not found',
                                game=self)
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
                            invalid_input('Place not recognized.',
                                input_string=travel_location,
                                tag='room specified not found',
                                game=self)
                            
            if command.verb.name == 'stats':
                print ' ### USER STATS ### '
                self.player.player_status()
                print ' ### GAME STATS ### '
                print 'game started : ', self.GAME_START
                print 'commands entered : ', self.commands_entered

            if command.verb.name == 'quests':
                user_input.get_events_list(self)

            if command.verb.name == 'help':
                user_input.help_info()

            if command.verb.name == 'location':
                self.player.player_location()

            if command.verb.name == 'inventory' or command.verb.name == 'bag':
                print self.player.inventory.list_of_items()

            if command.verb.name == 'save':
                self.save_game()

            if command.verb.name == 'name':
                print self.player.name

            else:
                print "I'm not sure what you mean."

            self.commands_entered += 1
        else:
            invalid_input('Command not recognized.',
                input_string=command.raw,
                tag='unknown command',
                game=self)