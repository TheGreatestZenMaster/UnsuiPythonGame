# should print immediately to demonstrate usage.
from lib.eventsEngine.EventsEngine import Event, Action, Trigger


def get_event(game):
    return Event(
            Trigger( 'True'),
            Action('print "The event engine is working!"')
        )