import ConfigParser
import os
from rooms.Room import Room
from items.Item import Item

class UnsuiConfigParser(ConfigParser.ConfigParser):
    def getlist(self,section,option):
        value = self.get(section,option)
        return list(filter(None, (x.strip() for x in value.splitlines())))


class UnsuiConfigLoader(object):
    def __init__(self):
        self.known_types = ["room", "item"]
        self.config = UnsuiConfigParser()
        self.loaded_data = {'room' : [], 'item' : []}

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
            contents_list.append(self.get_by_type_and_name('item', item))
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
