import ConfigParser
import os
from rooms.Room import Room
from items.Item import Item
from Player.Player import Player
from Player.Inventory import Inventory

class UnsuiConfigParser(ConfigParser.ConfigParser):
    def getlist(self,section,option):
        value = self.get(section,option)
        return list(filter(None, (x.strip() for x in value.splitlines())))


class UnsuiConfigLoader(object):
    """
    Loads objects into memory from config files
    Current supported: Room, Item

    TODO:
        - Support NPC Class and Dialogue systems
    """
    def __init__(self):
        self.known_types = ["room", "item"]
        self.config = UnsuiConfigParser()
        self.loaded_data = {'room' : [], 'item' : []}

        self.unpopulated_rooms = []

    def load(self):
        for section in self.config.sections():
            for option in self.config.options(section):
                if self.config.get(section, option) in self.loaded_data:
                    # Creates room objects from config file
                    if self.config.get(section, option) == 'room':
                        self.loaded_data['room'].append(self.create_room(section))
                    # Creates item objects from config file
                    if self.config.get(section, option) == 'item':
                        self.loaded_data['item'].append(self.create_item(section))

    def create_room(self, section):
        """Returns a Room instance."""
        contents_list = []
        for item in self.config.getlist(section, "contents"):
            if item == "None":
                break
            try:
                contents_list.append(self.get_by_type_and_name('item', item))
            except ValueError:
                self.unpopulated_rooms.append([self.config.get(section, "name"), self.config.getlist(section, "contents")])
                contents_list = []
                break
        return Room(self.config.get(section, "name"), self.config.get(section, "description"), self.config.getlist(section, "exits"), contents_list)

    def create_item(self, section):
        """Returns a Item instance."""
        try:
            a = self.config.getlist(section, "contents")
            return Item(self.config.get(section, "id"), self.config.get(section, "name"), self.config.get(section, "description"), contents=a)
        except:
            return Item(self.config.get(section, "id"), self.config.get(section, "name"), self.config.get(section, "description"))

    def generate(self, level=False):
        """Traverses directory looking for .conf files and loads data from them"""
        if level == False:
            directory = os.path.dirname(os.path.realpath(__file__))
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.conf'):
                        self.config.read(os.path.join(root, file))
                        self.load()
            self.populate_rooms()
        else:
            directory = os.path.dirname(os.path.realpath(__file__))
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(level):
                        self.config.read(os.path.join(root, file))
                        self.load()
            self.populate_rooms

    def populate_rooms(self):
        """"""
        for room in self.unpopulated_rooms:
            for item in room[1]:
                try:
                    self.get_by_type_and_name('room', room[0]).inventory.add_item(self.get_by_type_and_name('item', item))
                except ValueError:
                    pass

    def get_by_type(self, type):
        return self.loaded_data[type]

    def get_by_type_and_name(self, type, name):
        for item in self.loaded_data[type]:
            if item.name.lower() == name.lower():
                return item
            else:
                pass
        else:
            raise ValueError('Cannot find '+str(type)+' '+str(name))

    def save_game(self, player):

        config = UnsuiConfigParser()

        # Save rooms
        for room in self.loaded_data['room']:
            config.add_section(room.name)
            config.set(room.name, 'type', 'room')
            config.set(room.name, 'name', room.name)
            config.set(room.name, 'description', room.description)
            config.set(room.name, 'exits', ', '.join(room.exits))

            config.set(room.name, 'contents', ', '.join(room.inventory.list_of_items_by_name()))

        # Save items
        for item in self.loaded_data['item']:
            config.add_section(item.name)
            config.set(item.name, 'type', 'item')
            config.set(item.name, 'id', item.id)
            config.set(item.name, 'name', item.name)
            config.set(item.name, 'description', item.description)

        # Save player
        config.add_section('player')

        config.set('player', 'inventory', ', '.join(player.inventory.list_of_items_by_name()))
        config.set('player', 'name', player.name)
        config.set('player', 'race', player.race)
        config.set('player', 'sex', player.sex)
        config.set('player', 'current_location', player.current_location.name)

        config.set('player', 'health', player.health)
        config.set('player', 'max_hp', player.max_hp)
        config.set('player', 'attack', player.attack)
        config.set('player', 'base_attack', player.base_attack)
        config.set('player', 'armour', player.armour)
        config.set('player', 'xp', player.xp)
        config.set('player', 'level', player.level)
        config.set('player', 'status', player.status)
        config.set('player', 'base_xp', player.base_xp)

        with open('example_save.conf', 'wb') as configfile:
            config.write(configfile)

    def load_game(self, savefile):
        self.generate(level=savefile)

    def create_player(self):
        name = self.config.get('player', 'name')
        race = self.config.get('player', 'race')
        sex = self.config.get('player', 'sex')
        current_location = self.get_by_type_and_name('room', self.config.get('player', 'current_location')) 
        loaded_player = Player(name, race, sex, current_location)
        loaded_player.inventory = Inventory()
        for item in self.config.getlist('player', 'inventory'):
            loaded_player.inventory.add_item(self.get_by_type_and_name('item', item))

        loaded_player.health = self.config.getint('player', 'health')
        loaded_player.max_hp = self.config.getint('player', 'max_hp')
        loaded_player.attack = self.config.getint('player', 'attack')
        loaded_player.base_attack = self.config.getint('player', 'base_attack')
        loaded_player.armour = self.config.getint('player', 'armour')
        loaded_player.xp = self.config.getint('player', 'xp')
        loaded_player.level = self.config.getint('player', 'level')
        loaded_player.status = self.config.get('player', 'status')
        loaded_player.base_xp = self.config.getint('player', 'base_xp')

        return loaded_player          