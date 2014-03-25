
class Inventory(object):
    def __init__(self):
        self.items = list()
    def add_item(self,item):
        if item != None:
            self.items.append(item)
