#    _   _                 _ 
#   | | | |               (_)
#   | | | |_ __  ___ _   _ _ 
#   | | | | '_ \/ __| | | | |
#   | |_| | | | \__ \ |_| | |
#    \___/|_| |_|___/\__,_|_|


#----- Base Python imports ------#

#----- Set path to library ------#
import os
import sys

#----- Unsui imports ------#
import user_input
from GameInstance import GameInstance, DEFAULT_SAVE_FILE
from send_data import invalid_input

#----- Library imports -----#
import lib.colorama as colorama

colorama.init(autoreset=True)


def upper_main(player_game, input=raw_input):
    """
    This loop should never exit.
    Exception: if the player specifies to exit
    """
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
        print '"Load" existing game or "start" new game?'
        input_string = raw_input("load/start? ")
        if input_string == 'load' or input_string == 'l':
            player_game = GameInstance(load=DEFAULT_SAVE_FILE)
            upper_main(player_game)
        elif input_string == 'start' or input_string == 's':
            player_game = GameInstance()
            upper_main(player_game)
        else:
            invalid_input("Please enter \"load\" or \"start\"",
                input_string=input_string,
                tag='bad load/save choice') 

#------- Game Operation --------#
if __name__ == '__main__':
    splash_screen()

    
