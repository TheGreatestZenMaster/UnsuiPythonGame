''' 
Action class for events. 
'''

### ACTIONS ###
def printout(text,remove=True):
    print text
    
    

class Action(object):
    
    def __init__(self,function,*args):
        '''
        function : the trigger function (must return boolean)
        *args : arguments for the trigger function
        '''
        self.function = function
        self.args = args
        
    def __call__(self):
        self.function(*self.args)
      
