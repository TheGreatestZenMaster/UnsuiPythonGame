from Unsui import *

import unittest
import string
import random
from nose.tools import raises

from items.Key import Key

def randomString(prompt='', size=6, chars=string.printable):
    '''
    Returns a randomly generated string of given size using specified given charset.
    NOTE: string.printable = string.letters + string.digits + string.whitespace + string.punctuation
    '''
    return ''.join(random.choice(chars) for _ in range(size))

def alwaysExit(prompt=''):
    return 'exit'
    
class doesItRun(unittest.TestCase):

    @raises(SystemExit)  # because of systemExit
    def exit_upper_main_test(self):
        upper_main(player_game, input=alwaysExit)