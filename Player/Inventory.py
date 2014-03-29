class Inventory(object):
    def __init__(self):
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def remove_item(self, item):
        self.contents.remove(item)

    def list_of_items(self, item_type='all', return_type='object'):
        return_list = []
        for item in self.contents:
            return_list.append(item)
        return return_list

    def list_of_items_by_name(self):
        return_list = []
        for item in self.contents:
            return_list.append(item.name)
        return return_list

    def list_of_items_by_type(self, item_type):
        return_list = []
        for item in self.contents:
            if item.type == item_type:
                return_list.append(item.name)
        return return_list

    def current_inventory(self):
        if len(self.items) > 0:
            for item in self.items:
                print "In your inventory, there is a...", item.name
        else:
            print "Your inventory is empty!"