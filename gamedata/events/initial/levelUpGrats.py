# tells user 'grats' for 1st level up
from lib.eventsEngine.EventsEngine.EventsEngine import Event, Action, Trigger


def get_event(game):
    return Event(
            Trigger( 'o.player.level > 1', game),
            Action('print "Nice! You leveled up!"')
        )