'''
First quest is designed to be a tutorial of sorts. It might include:
        >shower
        >dress
        >eat
        >find something or another
'''

from events.Story import Story
from events.Event import Event
from events.eventAction import Action, printout
from events.Trigger import Trigger, locationIs, alwaysTrue

def first_quest(game):
    '''
    currently the first quest is to visit all rooms...
    '''
    eventList = [
        Event(Trigger(alwaysTrue), # this prints the first time checkEvents is called (right after first user input)
            Action(printout,'First things first, better get some pants on, right? Do you see them?')),
        Event(Trigger(alwaysTrue), # this prints after the next command
            Action(printout,'I guess they aren\'t here, I guess the devs need to work on this. Better explore some more.')),
        Event(Trigger(locationIs,game,'Hallway'),
            Action(printout,'Yep... The good old hallway. It is a great place for going other places. Speaking of going, I think you have something to take care of in the bathroom.')),
        Event(Trigger(locationIs,game,'Bathroom'),
            Action(printout,'Ahhh... That\'s better. You should probably brush your teeth and shower, but what the hell... you\'re feeling gutsy.')),
        Event(Trigger(alwaysTrue),
            Action(printout,'Your stomach grumbles...')),
        Event(Trigger(locationIs,game,'Kitchen'),
            Action(printout,'This is where food should be, right? Where is everything? What, do these game devs have lives outside of coding this game? pssh. Well hopefully they at least put something interesting in the Living Room.')),
        Event(Trigger(locationIs,game,'Living Room'),
            Action(printout,'...Nope... Nothing here...')),
        Event(Trigger(alwaysTrue),
            Action(printout,'Congratulations! You\'ve completed your first quest: "Morning Routine"!'))
    ]

    return Story(eventList)
    
