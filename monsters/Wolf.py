from monsters.Monster import Monster

class Wolf(Monster):
    def __init__(self, name, room):
        self.self = self
        self.room = room
        self.name = name

        self.health = 0
        self.max_hp = 0
        self.attack = 0
        self.base_attack = 0
        self.armour = 0
        self.xp = 0
        self.level = 0
        self.status = "Alive"

    def level_up(self):
        new_level_health = 20
        new_level_hp = 20
        new_level_attack = 5
        new_level_base_attack = 5
        new_level_armour = 0
        new_level_xp = 10

        self.health += new_level_health
        self.max_hp += new_level_hp
        self.attack += new_level_attack
        self.base_attack += new_level_base_attack
        self.armour += new_level_armour
        self.xp += new_level_xp
        self.level += 1

    def attack(self):
        player.health -= (self.attack - player.armour)
        if player.health <= 0:
            print "You have died! Better luck next time!"
            sys.exit()

