from user_input import choose_object
import unittest

from items.Key import Key

class basic_UI_tests(unittest.TestCase):

    def random_setup_test(self):
        '''
        runs through basic setup with random values
        '''
        print 'yeah... i need to do this... later... =)'
        # raise NotImplementedError()
    
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
