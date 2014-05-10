# should print immediately to demonstrate usage.
from eventsEngine.EventsEngine.Event import Event
from eventsEngine.EventsEngine.Trigger import Trigger
from eventsEngine.EventsEngine.Action import Action


def get_event(game):
    return Event(
            Trigger( 'True'),
            Action('print "The event engine is working!"')
        )