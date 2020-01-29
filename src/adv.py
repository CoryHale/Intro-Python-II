from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     []),

    'foyer':    Room("Foyer", 
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    [Item("Torch", "the torch is emitting a warm glow which lights up the room"),
                    Item("Sword", "the old sword is a bit dull and slightly rusted")]),

    'overlook': Room("Grand Overlook", 
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    [Item("Key", "the gold key appears to shine in the dark")]),

    'narrow':   Room("Narrow Passage", 
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    [Item("Shield", "the wooden shield is rotting in places but still feels sturdy")]),

    'treasure': Room("Treasure Chamber", 
                    """You've found the long-lost treasure chamber! A large gilded chest sits in the middle of the room, it looks as though it needs a key. The only exit is to the south.""",
                    [Item("Treasure", "the 5000 gold pieces and diamonds, rubies, and emeralds look fit for a King!")]),
}


# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['foyer'].s_to = 'outside'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Input your player name: ").strip()
print("\n")

my_player = Player(player_name, "outside", [])

# Write a loop that:

playing = True

while playing:

# * Prints the current room name

    cur_room = my_player.current_room

    if cur_room == "outside":
        print(f"{my_player.name} is now {room[cur_room].name}")

    else:
        print(f"{my_player.name} is now in the {room[cur_room].name}")
        

# * Prints the current description (the textwrap module might be useful here).

    print(room[cur_room].description)
    print("\n")

# Prints the items in the room.

    if room[cur_room].item_list.__len__() > 0:
        print("You find these items in the room: ")
        for i in room[cur_room].item_list:
            print(f"{i.name} - {i.description}")
        print("\n")
    
    elif room[cur_room].item_list.__len__() == 0 and cur_room != 'outside':
        print("There aren't any items in this room.")

# * Waits for user input and decides what to do.

    com = input("What would you like to do: ").lower().strip()
    print("\n")

# Checks to see if 1 or 2 words were entered.

    com_len = com.split()

    if com_len.__len__() == 1:

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

        if com.__len__() > 1 or com.__len__() == 0:
            print("Here are the commands you can use:")
            print("\t'n': North")
            print("\t'e': East")
            print("\t's': South")
            print("\t'w': West")
            print("\t'i': Inventory")
            print("\t'q': Quit Game")

        if com == "n":
            if room[cur_room].n_to != None:
                my_player.current_room = room[cur_room].n_to

            else:
                print("You cannot move this direction. Try Again.")
                print("\n")
                
        elif com == "e":
            if room[cur_room].e_to != None:
                my_player.current_room = room[cur_room].e_to

            else:
                print("You cannot move this direction. Try Again.")
                print("\n")

        elif com == "s":
            if room[cur_room].s_to != None:
                my_player.current_room = room[cur_room].s_to

            else:
                print("You cannot move this direction. Try Again.")
                print("\n")

        elif com == "w":
            if room[cur_room].w_to != None:
                my_player.current_room = room[cur_room].w_to

            else:
                print("You cannot move this direction. Try Again.")
                print("\n")

# If the user enters "i", show them their inventory.

        elif com == "i":
            if my_player.inventory.__len__() > 0:
                print(f"{my_player.name}'s inventory: ")
                for i in my_player.inventory:
                    print(f"{i.name} - {i.description}")
                print("\n")
            
            else:
                print(f"{my_player.name}'s inventory is empty")
                print("\n")

# If the user enters "q", quit the game.

        elif com == "q":
            print("Thank you for playing the game! Hope to see you soon!")
            playing = False

# Inventory commands.

    if com_len[0] == 'get' or com_len[0] == 'take':
        exists = False
        index = 0
        for i in room[cur_room].item_list:
            if com_len[1].lower() == i.name.lower():
                item = room[cur_room].item_list.pop(index)
                my_player.inventory.append(item)
                item.on_take(item.name)
                exists = True
            index += 1
        
        if exists == False:
            print("This item is not in room")

    elif com_len[0] == 'drop':
        exists = False
        index = 0
        for i in my_player.inventory:
            if com_len[1].lower() == i.name.lower():
                item = my_player.inventory.remove(index)
                room[cur_room].item_list.append(item)
                item.on_drop(item.name)
                exists = True
            index += 1

        if exists == False:
            print("This item is not in inventory")



