from parser import Parser

import sys
import os
sys.path.append( os.getcwd() + '\\lib')

import output_formatter

default_input = raw_input

def request_action(game,input=default_input):
    '''
    This is used to ask the user to choose an action.
    Returns requested user action.
    '''
    
    print "Your available actions while in the %s are %s" % (game.player.current_location.name, 
                                                            game.actions_available)
    return input("What do you want to do? ")
    

def choose_object(item_list, input=default_input):
    '''
    prompts the user to choose an object from the given list
    '''
    grab_object = input("Grab what?")
    for item in item_list:
        if grab_object.lower() == item.name.lower():
            print "You grabbed it!"
            item_list.remove(item)
            return item
    else:
        print "can't find it!"
        return None
        
def opening_setup(game, input=default_input):
    """This opening setup gives us a player name and also provides the opening text"""
    name = input("Whats your name?")
    starting_room = game.config_loader.get_by_type_and_name('room', "Bedroom")
    game.player.name = name
    game.player.current_location = starting_room
    game.player.player_location()
    # The opening text to give a little story(will change later once we have some actual story)
    opening_text = "Hello and welcome to your adventure {}!\n" \
                   "Its a bright new day! Lets get to it!".format(game.player.get_name())
    output_formatter.print_c(opening_text)
    game.player.level_up() 

#------Help function ------#
def help_info(input=default_input):
    """Provides a information about the available prompts should the player need it"""
    help_info_dict = {"enter": "This command will move your character into the next room.",
                      "exit": "This command exits the game! Careful!",
                      "stats": "This command provides you with info about your character.",
                      "grab": "This command lets you grab any object. Simply say which one.",
                      "leave": "This command lets you leave through any unlocked door",
                      "doors": "This command shows you what doors are visible.",
                      "keys": "This command show you any keys you can see.",
                      "location": "This command tells you your current location.",
                      "fight": "This command lets you fight the monster",
                      "help": "show this menu",
                      "go": "Travel to a room of your choice"
                      }
    while True:
        info_choice = input("What would you like to know more about? ('back' returns you to the prompt)").lower()
        try:
            print help_info_dict[info_choice]
        except KeyError:
            if info_choice == "back":
                return False
            else:
                print "That's not a valid command! type 'back' to exit help."
