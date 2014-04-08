from user_input import choose_object, opening_setup, help_info
from GameInstance import GameInstance, BASE_ACTIONS

import unittest
import string
import random

from items.Key import Key

def randomString(prompt='', size=6, chars=string.printable):
    '''
    Returns a randomly generated string of given size using specified given charset.
    NOTE: string.printable = string.letters + string.digits + string.whitespace + string.punctuation
    '''
    return ''.join(random.choice(chars) for _ in range(size))

    

class UI_tests(unittest.TestCase):

    def random_setup_test(self):
        '''
        runs through basic setup with random values to ensure it does not crash
        '''
        game = GameInstance(input_func=randomString)
        
    
    def grab_object_test(self):
        testItem = Key("key1", "Room 1", 10001)
        
        items = [testItem]
        
        def badChoice(prompt):
            return "notItem"

        def goodChoice(prompt):
            return "key1"
        
        self.assertEqual(choose_object(items, badChoice), None)
        self.assertEqual(choose_object(items, goodChoice), testItem)
        # item1 should now not be in the list anymore...
        self.assertEqual(choose_object(items, goodChoice), None)
        
    def base_help_test(self):
        '''tests out the help for all base actions'''
        game = GameInstance(input_func=randomString)
        
        for action in BASE_ACTIONS:
            class pickAction(object):
                def __init__(self):
                    self.choice = action
                def __call__(self,prompt):
                    if self.choice == action:
                        self.choice = 'back'
                        return action
                    elif self.choice == 'back':
                        self.choice == None
                        return 'back'
                    else:
                        raise Error('WAT')
            chooser = pickAction()
            help_info(input=chooser)

    def base_actions_test(self):
        ''' test to ensure that base actions don't crash '''
        game = GameInstance(input_func=randomString)
        
        for action in BASE_ACTIONS:
            if action=="exit": # skip exit action (or else test breaks)
                continue
            elif action=="help": # ignore help
                continue
            else:
                command = game.parser.parse(action)
                game.take_action(command,input=randomString)
            
            