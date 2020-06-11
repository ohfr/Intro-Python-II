# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def seeItems(self):
        for item in self.items:
            print(item)

    def findItem(self, item):
        for i in self.items:
            if i.name == item:
                return i
        
    def removeItem(self, item):
        self.items.remove(item)
