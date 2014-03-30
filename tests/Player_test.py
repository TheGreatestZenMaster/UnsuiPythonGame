''' unit test for the Player class '''

import unittest
from random import randrange

from Player.Player import Player, max_level

class basic_leveling_check(unittest.TestCase):

    def test_level_growth(self):
        """ tests that all stats are >= those of previous level (for 1st n levels)"""
        n = 10 # number of levels to test
        
        p1 = Player('p1','elf')
        
        for level in range(n):
            h = p1.health
            hp= p1.max_hp
            a = p1.attack
            ba= p1.base_attack
            ar= p1.armour
            l = p1.level
            
            p1.level_up()
            
            self.assertTrue(p1.health >= h)
            self.assertTrue(p1.max_hp >= hp)
            self.assertTrue(p1.attack >= a)
            self.assertTrue(p1.base_attack >= ba)
            self.assertTrue(p1.armour >= ar)
            self.assertTrue(p1.level >= l)

    def test_levelup_by_one(self):
        '''
        tests that player.levelup() increases level by one 
        for randomly chosen level.
        '''
        p1 = Player('p1','elf')
        
        # set p1 to random level
        for i in range(randrange(max_level-1)):
            p1.level_up()
        l = p1.level
        p1.level_up()
        self.assertEqual(p1.level - l, 1)
