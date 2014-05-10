''' 
Functions for getting at all the event (& story!) data easily.
'''
import pkgutil

import events.initial
import stories.initial

def getStartingEvents(game):
    ''' return list of all initial events and stories '''
    from .events.initial import *
    from .stories.initial import *

    eventlist = []
    
    package = events.initial
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        eventlist.append(eval(modname+'.get_event(game)'))
        
    package = stories.initial
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        eventlist.append(eval(modname+'.get_event(game)'))

    return eventlist