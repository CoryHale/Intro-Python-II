from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

my_player = Player("outside")

# Write a loop that:

playing = True

while playing:

# * Prints the current room name

    cur_room = my_player.current_room
    print(room[cur_room].name)

# * Prints the current description (the textwrap module might be useful here).

    print(room[cur_room].description)

# * Waits for user input and decides what to do.

    dir = input("Enter a direction: ").lower().strip()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

    if dir == "n":
        if room[cur_room].n_to != None:
            my_player.current_room = room[cur_room].n_to

        else:
            print("You cannot move this direction. Try Again.")
            
    elif dir == "e":
        if room[cur_room].e_to != None:
            my_player.current_room = room[cur_room].e_to

        else:
            print("You cannot move this direction. Try Again.")

    elif dir == "s":
        if room[cur_room].s_to != None:
            my_player.current_room = room[cur_room].s_to

        else:
            print("You cannot move this direction. Try Again.")

    elif dir == "w":
        if room[cur_room].w_to != None:
            my_player.current_room = room[cur_room].w_to

        else:
            print("You cannot move this direction. Try Again.")

    elif dir == "q":
        print("Thank you for playing the game! Hope to see you soon!")
        playing = False



# If the user enters "q", quit the game.


