class Inventory(object):
    def __init__(self):
        self.items = list()

    def add_item(self, item):
        if item != None:
            self.items.append(item)
            print "The %s was added to your inventory!" % item.name

    def remove_item(self, item):
        for remove_item in self.items:
            if item == remove_item.name:
                self.items.remove(remove_item)
                print "The %s was removed from your inventory." % remove_item.name
                break
            else:
                print "something is wrong"

    def current_inventory(self):
        if len(self.items) > 0:
            for item in self.items:
                print "In your inventory, there is a...", item.name
        else:
            print "Your inventory is empty!"