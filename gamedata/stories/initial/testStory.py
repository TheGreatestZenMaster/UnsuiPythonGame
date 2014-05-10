# should print immediately to demonstrate usage.
from lib.eventsEngine.EventsEngine import Story, Event, Action, Trigger


def get_event(game):
    eventlist = [
        Event(
            Trigger('True'),  # this prints the first time checkEvents is called (right after first user input)
            Action('print "First things first, better get some pants on, right? Do you see them?"')
        ),
        Event(
            Trigger('True'),  # this prints after the next command
            Action('print "I guess they aren\'t here, I guess the devs need to work on this. Better explore some more."')
        ),
        Event(
            Trigger('o.player.current_location.name == "Hallway"', game),
            Action('print "Yep... The good old hallway. It is a great place for going other places. Speaking of going, I think you have something to take care of in the bathroom."')
        ),
        Event(
            Trigger('o.player.current_location.name == "Bathroom"', game),
            Action('print "Ahhh... That\'s better. You should probably brush your teeth and shower, but what the hell... you\'re feeling gutsy."')
        ),
        Event(
            Trigger('True'),
            Action('print "Your stomach grumbles..."')
        ),
        Event(
            Trigger('o.player.current_location.name == "Kitchen"', game),
            Action('print "This is where food should be, right? Where is everything? What, do these game devs have lives outside of coding this game? pssh. Well hopefully they at least put something interesting in the Living Room."')
        ),
        Event(Trigger('o.player.current_location.name == "Living Room"', game),
            Action('print "...Nope... Nothing here..."')
        ),
        Event(Trigger('True'),
            Action('print "Congratulations! You\'ve completed your first quest: \"Morning Routine!\""')
        )
    ]
    return Story(eventlist)