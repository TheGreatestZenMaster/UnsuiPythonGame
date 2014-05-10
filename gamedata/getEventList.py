''' 
Functions for getting at all the event (& story!) data easily.
'''
import pkgutil

from .events import initial
from .events.initial import *
# from quests.first_quest import first_quest

def getStartingEvents(game):
    ''' return list of all initial events and stories '''
    eventlist = []
    
    package = initial
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        eventlist.append(eval(modname+'.get_event(game)'))
        
    # TODO: do the same with stories
        
    return eventlist