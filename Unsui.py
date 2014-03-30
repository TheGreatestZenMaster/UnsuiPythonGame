#----- Base Python imports ------#

#----- Set path to library ------#
import os
import sys

#----- Unsui imports ------#
import user_input
from GameInstance import GameInstance

#----- Library imports -----#
import lib.colorama as colorama

colorama.init()
player_game = GameInstance()

def upper_main(player_game, input=raw_input):
    """
    This loop should never exit.
    Exception: if the player specifies to exit
    """
    user_input.opening_setup(player_game,input)
    while True:
        user_action = user_input.request_action(player_game,input)
        if not user_action == "":
		    # Commands are interpreted after being parsed into a Command object
            command = player_game.parser.parse(user_action)
            player_game.take_action(command)



#------- Game Operation --------#
if __name__ == '__main__':
    upper_main(player_game)
