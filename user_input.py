# unsui imports #
from input_parser import Parser
from send_data import invalid_input

# lib imports #
from lib.colorama.colorama import Fore

# globals #
default_input = raw_input


def request_action(game,input=default_input):
    '''
    This is used to ask the user to choose an action.
    Returns requested user action.
    '''
    
    print("Your available actions while in the "
        +Fore.GREEN+"{}".format(game.player.current_location.name)
        +Fore.RESET+" are:\n"
        +Fore.CYAN+"{}".format(game.actions_available))
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
        invalid_input("can't find it!",
            input_string=grab_object,
            tag='request to grab unknown object',
            extra='avail_choices='+str(item_list)) 
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
    print opening_text
    game.player.level_up() 


def get_events_list(game):
        '''
        Prints out the list of current initiated events
        '''
        print("You have the following quests")
        for event in game.events:
            if event.initiated and not event.completed:
                print(event.get_event_name())


#------Help function ------#
def help_info(input=default_input):
    """Provides a information about the available prompts should the player need it"""
    help_info_dict = {"go": "This command will move your character to another room of your choice.",
                      "exit": "This command exits the game! Careful!",
                      "stats": "This command provides you with info about your character.",
                      "location": "This command tells you your current location.",
                      "help": "show this menu",
                      }
    while True:
        info_choice = input("What would you like to know more about? ('back' returns you to the prompt)").lower()
        try:
            print help_info_dict[info_choice]
        except KeyError:
            if info_choice == "back":
                return False
            else:
                invalid_input("That's not a valid command! type 'back' to exit help.",
                    input_string=info_choice,
                    tag='unknown help request') 
