''' 
a hacky way to get events working while we try to think of something
more clever.
'''
import datetime

from Event import Event
from Trigger import Trigger, playerLevelAbove, locationIs, allwaysTrue, commandCountAbove, timeElapsedSinceGameStart
from eventAction import Action, printout

def getEventList(game):
    ''' return list of all events '''
    return [
        Event(Trigger(allwaysTrue), 
            Action(printout,'Hey! You can type... this is a good sign.')),
        Event(Trigger(commandCountAbove,game,2),
            Action(printout,"Oh! You're still here! Awesome.")),
        Event(Trigger(timeElapsedSinceGameStart,game,datetime.timedelta(weeks=104)),
            Action(printout,"Remember when we first started this journey? Over TWO YEARS ago? Yeah... those were the days...")),
        Event(Trigger(playerLevelAbove,game,1),
            Action(printout,'Nice! You leveled up!')),
        Event(Trigger(locationIs,game,'Hallway'),
            Action(printout,'Wow! Your first time in the hallway!'))
        ]