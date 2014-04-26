''' unit test for the Player class '''

import unittest
import random

<<<<<<< HEAD
#from UnsuiPythonGame.send_data import *
=======
from send_data import *
>>>>>>> 584ddcf342f5db5e30803b06ca422ccb529ba393

class basic_tests(unittest.TestCase):

    def test_invalid_input_sender(self):
        """ tests that send_invalid_input throws no errors"""
        # some random junk to make me giggle later:
        silly_locations = [
            'over the rainbow',
            'behind you',
            '192.168.1.1',
            'your momma\'s house',
            '!#@$ if I know.',
            'the pub'
            ]
            
        # the actual test:
        #send_invalid_input('_tester_','tst str',random.choice(silly_locations),'unittest','-1','t'+str(['e']*random.randrange(7))+'st')
