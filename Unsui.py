#----- Base Python imports ------#
import sys

#----- Unsui imports ------#
import user_input
from GameInstance import GameInstance

game = GameInstance()
        
# Available actions for the loops
list_of_actions_available_room = ["grab", "leave", "stats", "location", "keys", "help"]



def upper_main(game,input=raw_input):
    """
    This loop should never exit.
    Exception: if the player specifies to exit
    """
    user_input.opening_setup(game,input)
    while True:
        user_input.request_action(game,input)


#------- Game Operation --------#
upper_main(game)
