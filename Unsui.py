#----- Base Python imports ------#

#----- Set path to library ------#
import os
import sys

#----- Unsui imports ------#
import user_input
from GameInstance import GameInstance

#----- Library imports -----#
import lib.colorama as colorama

colorama.init(autoreset=True)
player_game = GameInstance()

def upper_main(player_game, input=raw_input, load=False):
    """
    This loop should never exit.
    Exception: if the player specifies to exit
    """

    if not load:
        user_input.opening_setup(player_game,input)
    while True:

        user_action = user_input.request_action(player_game,input)
        if not user_action == "":
		    # Commands are interpreted after being parsed into a Command object
            command = player_game.parser.parse(user_action)
            player_game.take_action(command)
            player_game.check_events()
            
def splash_screen():
    '''
    display a simple splash screen which asks user to load/start game.
    '''
    while True:
        print "Load existing game or start new game?"
        input_string = raw_input("load/start? ")
        if input_string == 'load':
            player_game = GameInstance(load="example_save.conf")
            upper_main(player_game, load=True)
        if input_string == 'start':
            player_game = GameInstance()
            upper_main(player_game)
        else:
            print "Please enter \"load\" or \"start\""

#------- Game Operation --------#
if __name__ == '__main__':
    splash_screen()

    
