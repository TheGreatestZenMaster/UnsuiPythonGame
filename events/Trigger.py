''' 
Trigger class for events. 
'''
from datetime import datetime


### TRIGGER TEMPLATE FUNCTIONS ###
def alwaysTrue():
    return True

# player stats :
def playerLevelAbove(game,level):
    return game.player.level > level
    
def locationIs(game,loc):
    try:
        return game.player.current_location.name == loc
    except AttributeError:
        return False
    
# game stats :
def commandCountAbove(game,number):
    return game.commands_entered > number

def timeElapsedSinceGameStart(game,timeDelta):
    return (datetime.now() - game.GAME_START) > timeDelta
    
    

class Trigger(object):
    
    def __init__(self,function,*args):
        '''
        function : the trigger function (must return boolean)
        *args : arguments for the trigger function
        '''
        self.function = function
        self.args = args
        
    def __call__(self):
        return self.function(*self.args)
      
