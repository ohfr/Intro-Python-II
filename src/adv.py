from room import Room

from player import Player

from item import Item

# Declare all the rooms

sword = Item("Sword", "Sharp and deadly")

axe = Item("Axe", "Heavy and brutal")

staff = Item("Staff", "Quick and nimble")

gold = Item("Gold", "The best kind of treasure")

diamond = Item("Diamond", "Pure and beautiful")


outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons", [sword, axe])

foyer = Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [staff])

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

treasure =  Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [gold, diamond])


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow .w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#
playerName = input("Please choose a name for your character\n")
# # Make a new player object that is currently in the 'outside' room.
player = Player(playerName, outside)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

validDirections  = ('n', 's', 'e', 'w')

#old move rooms function
# try:
#     if direction == 'n':
#         player.current_room = player.current_room.n_to
#     elif direction == 's':
#         player.current_room = player.current_room.s_to
#     elif direction == 'e':
#         player.current_room = player.current_room.e_to
#     elif direction == 'w':
#         player.current_room = player.current_room.w_to
#     else:
#         direct = input("Please enter a valid direction, directions are n, s, e, w")
#         return moveRooms(direct)
# except AttributeError:
#     direct = input("You have chosen an empty path, please pick another\n")
#     return moveRooms(direct)



def moveRooms(direction):
    if direction in validDirections:
        if hasattr(player.current_room, f'{direction}_to') and getattr(player.current_room, f'{direction}_to') is not None:
            player.current_room = getattr(player.current_room, f'{direction}_to')
        else:
            direct = input("You have chosen an empty path, please pick another\n")
            return moveRooms(direct)
    else:
        direct = input("Please enter a valid direction, directions are n, s, e, w\n")
        return moveRooms(direct)


def itemAction(action, item):
    if action == 'get' or action == 'take':
        if getattr(player.current_room, "items") is not None:
            foundItem = player.current_room.findItem(item)
            if foundItem is not None:
                player.current_room.removeItem(foundItem)
                player.getItem(foundItem)
                foundItem.on_take()
            else:
                print(f"There is no {item} in this room")
        else:
            print(f"There is no {item} in this room")
    elif action == 'drop':
        if player.items is not None:
            foundItem = player.itemCheck(item)
            if foundItem is not None:
                player.dropItem(foundItem)
                foundItem.on_drop()
            else:
                print(f"You do not have {item} in your inventory")
        else:
            print("Your inventory is currently empty")


while True:
    direction = input("What's your next move?\n")
    
    if direction in validDirections:
        moveRooms(direction)
        player.printCurrentRoom()
    elif " " in direction:
        action, item = direction.split(" ")
        itemAction(action, item) 
    elif direction == 'i' or direction == 'inventory':
        player.getInventory()
    elif direction == 'q':
        break


    