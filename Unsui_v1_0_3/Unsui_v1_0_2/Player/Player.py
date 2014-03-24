
from Inventory import Inventory

max_level = 100

# constants used to base stats increases on during level changes.
new_level_health = 50
new_level_hp = 50
new_level_attack = 10
new_level_base_attack = 10
new_level_armour = 5

class Player(object):
    """Base Class for the player"""
    
    def __init__(self, name=None, race=None, sex=None, current_location=None):
        self.inventory = Inventory()

        self.name = name
        self.race = race
        self.sex = sex
        self.current_location = current_location
        
        self.health = 0
        self.max_hp = 0
        self.attack = 0
        self.base_attack = 0
        self.armour = 0
        self.xp = 0
        self.level = 0
        self.status = "Alive"
        self.base_xp = 0
        
    def level_up(self):
        '''
        increases stats to next level.
        currently this assumes that levels scale linearly to infinity.
        '''

        self.health += new_level_health
        self.max_hp += new_level_hp
        self.attack += new_level_attack
        self.base_attack += new_level_base_attack
        self.armour += new_level_armour
        self.level += 1
                
    def attack(self, monster):
        monster.health -= (self.attack - monster.armour)
        if monster.health <= 0:
            print "You beat the monster!"
            player.xp += monster.xp
            prompt_levelup()
            return False
        
    def player_status(self):
        print "Your stats are:\nHealth: %r, Armour: %r, Attack: %r, Level: %r, Experience: %r" % \
              (self.health, self.armour, self.attack, self.level, self.xp)    

    def player_location(self):
        print "You are in %r" % self.current_location