''' 
A base event class. 
Subclasses should implement abstract methods "trigger" and "action".
'''

class Event(object):
    
    def __init__(self,trigger=None,action=None):
        self.trigger = trigger
        self.action  = action
        
    def check(self):
        ''' checks the event for trigger condition satisfied '''
        if self.trigger():
            self.action()
            return True
        # else do nothing
            
    def trigger(self):
        raise NotImplementedError('Abstract method "trigger" should be implemented by subclass')
        
    def action(self):
        raise NotImplementedError('Abstract method "action" should be implemented by subclass')