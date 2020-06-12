# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items=None, score=0):
        self.name = name
        self.current_room = current_room
        self.items = items
        self.score = score

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def printCurrentRoom(self):
        print(f"You are currently in the {self.current_room} room, {self.current_room.description}")

    def getInventory(self):
        if self.items is not None:
            for item in self.items:
                print(f"You have a {item}")
        else:
            print("Inventory is empty")
    
    def getItem(self, item):
        if self.items is None:
            self.items = []
            
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)
    
    def itemCheck(self, item):
        for i in self.items:
            if i.name == item:
                return i
    def addScore(self):
        self.score +=1
