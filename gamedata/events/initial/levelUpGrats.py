# tells user 'grats' for 1st level up
from eventsEngine.EventsEngine.Event import Event
from eventsEngine.EventsEngine.Trigger import Trigger
from eventsEngine.EventsEngine.Action import Action


def get_event(game):
    return Event(
            Trigger( 'o.player.level > 1', game),
            Action('print "Nice! You leveled up!"')
        )