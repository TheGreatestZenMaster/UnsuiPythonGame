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
        Event(Trigger(alwaysTrue), # this prints the first time checkEvents is called (right after first user input)
            Action(printout,'First things first, better get some pants on, right?')),
        Event(Trigger(commandCountAbove,game,5),
            Action(printout,"Just a typical boring morning... Don't you wish you could break away from the daily grind?")),
        Event(Trigger(timeElapsedSinceGameStart,game,datetime.timedelta(weeks=104)),
            Action(printout,"Remember when we first started this journey? Over TWO YEARS ago? Yeah... those were the days...")),
        Event(Trigger(playerLevelAbove,game,1),
            Action(printout,'Nice! You leveled up!')),
        Event(Trigger(locationIs,game,'Hallway'),
            Action(printout,'Yep... The good old hallway. It is a great place for going other places.'))
        ]