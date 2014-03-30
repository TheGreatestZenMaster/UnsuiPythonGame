import ConfigParser
import os
from rooms.Room import Room
from items.Item import Item

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
        return Item(self.config.get(section, "id"), self.config.get(section, "name"), self.config.get(section, "description"))

    def generate(self):
        """Traverses directory looking for .conf files and loads data from them"""
        directory = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.conf'):
                    self.config.read(os.path.join(root, file))
                    self.load()
        self.populate_rooms()

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
