#----- Base Python imports ------#

#----- Unsui imports ------#
import user_input
from GameInstance import GameInstance

game = GameInstance()

def upper_main(game,input=raw_input):
    """
    This loop should never exit.
    Exception: if the player specifies to exit
    """
    user_input.opening_setup(game,input)
    while True:
        user_action = user_input.request_action(game,input)
        game.take_action(user_action)



#------- Game Operation --------#
upper_main(game)
