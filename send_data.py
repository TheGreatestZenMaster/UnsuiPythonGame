
import urllib, urllib2
from lib.colorama.colorama import Fore

from threading import Thread

UNSUI_VERSION = '0.1'   #TODO: I think there is a better place to keep this, but right now it isn't really used

def invalid_input(response, input_string='_', tag='_', game=None, extra='_'):
    '''
    this function should be used to tell the user when they have
    entered an invalid command or selection. Use of this function
    allows us to do neat things with the bad input_string rather
    than just throwing it away. Optional parameters should be used
    when convenient to provide additional data about the mis-input.
    
    # params: #
    response     = string message to print to user.
    
    # optional params: # 
    input_string = input string given by user
    tag          = programmer's unique description of error circumstance
    game         = gameInstance object associated with error
    extra        = additional information specific to the situation
    '''
    print(Fore.RED+response)
    
    try: # if game!=None and all is good
        playerName = game.player.name
        loc        = game.player.current_location.name
        cmd_count  = game.commands_entered
    except AttributeError: # if game==None or game is malformed
        playerName='?'
        loc='?'
        cmd_count='-1'
        
    send_invalid_input(playerName, input_string, loc, tag, cmd_count, extra)

def send_invalid_input(user_name, input_string, user_location, tag, command_count, extra):
    '''
    sends invalid input from user and user context information 
    to google form so that devs can handle commonly used
    unimplemented inputs.
    
    All paramters should be strings
    '''
    url = 'https://docs.google.com/forms/d/11c9-bSEC1bmC2_dlvZnAe3GxHdjkxQMDeFAjNV26DRQ/formResponse'
    form_data = {'entry.1027895744':input_string,
                'entry.474815179':user_location,
                'entry.1232903766':user_name,
                'entry.519998090':UNSUI_VERSION,
                'entry.420424348':tag,
                'entry.1770073495':command_count,
                'entry.1685744633':extra
                }
    data = urllib.urlencode(form_data)
    user_agent = "Unsui v"+UNSUI_VERSION
    header ={'User-Agent':user_agent}
    
    def sendIt(url,data,header):
        request = urllib2.Request(url, data, header)
        response = urllib2.urlopen(request)
        result = response.read()
    
    Thread(target=sendIt, args=(url,data,header)).start()
    
