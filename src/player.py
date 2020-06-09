# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def printCurrentRoom(self):
        print(f"You are currently in the {self.current_room} room, {self.current_room.description}")