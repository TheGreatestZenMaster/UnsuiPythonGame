''' 
a hacky way to get events working while we try to think of something
more clever.
'''
import datetime

from Event import Event
from Trigger import Trigger, playerLevelAbove, locationIs, alwaysTrue, commandCountAbove, timeElapsedSinceGameStart
from eventAction import Action, printout

def getEventList(game):
    ''' return list of all events '''
    return [
        Event(Trigger(commandCountAbove,game,7),
            Action(printout,"What a boring morning... Don't you wish you could break away from the daily grind?")),
        Event(Trigger(timeElapsedSinceGameStart,game,datetime.timedelta(weeks=104)),
            Action(printout,"Remember when we first started this journey? Over TWO YEARS ago? Yeah... those were the days...")),
        Event(Trigger(playerLevelAbove,game,1),
            Action(printout,'Nice! You leveled up!'))
        ]