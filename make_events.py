''' 
a hacky way to get events working while we try to think of something
more clever.
'''
from Event import Event
from Trigger import Trigger, playerLevelAbove, locationIs, allwaysTrue
from eventAction import Action, printout

def getEventList(game):
    ''' return list of all events '''
    return [
        Event(Trigger(allwaysTrue), 
            Action(printout,'Hey! You can type... this is a good sign.')),
        Event(Trigger(playerLevelAbove,game,1),
            Action(printout,'Nice! You leveled up!')),
        Event(Trigger(locationIs,game,'Hallway'),
            Action(printout,'Wow! Your first time in the hallway!'))
        ]