''' 
A base event class. 
Subclasses should implement abstract methods "trigger" and "action".
'''

class Event(object):
    
    def __init__(self,trigger=None,action=None):
        self.trigger = trigger
        self.action  = action
        self.initiated = False
        self.completed = False

        # currently set all events to start by default for testing
        self.event_start()
        
    def check(self):
        ''' checks the event for trigger condition satisfied '''
        if self.trigger():
            self.action()
            return True
        # else do nothing

    def event_start(self):
        self.initiated = True

    def event_end(self):
        self.completed = True

    def get_event_name(self):
        return self.trigger.function
            
    def trigger(self):
        raise NotImplementedError('Abstract method "trigger" should be implemented by subclass')
        
    def action(self):
        raise NotImplementedError('Abstract method "action" should be implemented by subclass')