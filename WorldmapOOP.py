class Room(object):
    # This is constructor
    def __init__(self, name, east=None, north=None, south=None, description="no", character='R19A'):
        # declared stuff on right not declared stuff on left
        self.name = name
        self.east = east
        self.north = north
        self.south = south
        self.description = description
        self.character = character


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """ This moves a player to a new location

        :param new_location: The room object that we move to
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A string (all lowercase), with a cardinal direction
        :return: A room object if it exists, None if it does not
        """
        return getattr(self.current_location, direction)


# These are the instances of the rooms (Instantiation)

# Option 1 - Use the Variables, but fix later
R19A = Room("Mr.Wiebe's Room")
parking_lot = Room("The parking lot", None, R19A)

R19A.north = parking_lot
# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("The parking lot", None, R19A)

player = Player(R19A)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
