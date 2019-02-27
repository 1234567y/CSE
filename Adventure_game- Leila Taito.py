class Room(object):
    def __init__(self, name, description=None, north=None, west=None, east=None, south=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south




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


Fresno = Room("Fresno", "One object in this room", None, None)
Kerman = Room("Kerman", "Leads to another room", Fresno, None)
LA = Room("LA", "Object here", Kerman, None)
SanFransisco = Room("SanFransisco", "Leads to another room", None, LA)
Washington = Room("Washington", "Leads to another room", None, SanFransisco)
Oregon = Room("Oregon", "Leads to another room", Washington, None)
Mexico = Room("Mexico", "Contains last object needed", None, Oregon)
Antioch = Room("Antioch", "Leads to another room", Mexico, None)
DailyCity = Room("DailyCity", "Leads to another room", None, Antioch)
Clovis = Room("Clovis", "Leads to another room", None, DailyCity)
Selma = Room("Selma", "Leads to another room", None, Clovis)
Hanford = Room("Hanford", "Leads to another room", Selma, None)
Dinuba = Room("Dinuba", "Leads to another room", Hanford, None)
Madera = Room("Madera", "Leads to another room", None, Dinuba)
Riverdale = Room("Riverdale", "This is where you can die.", Fresno, Madera)


Fresno.north = Riverdale
Fresno.west = Kerman
Kerman.north = LA
LA.south = SanFransisco
SanFransisco.east = Washington
Washington.west = Oregon
Oregon.south = Mexico
Mexico.north = Antioch
Antioch.east = DailyCity
DailyCity.south = Clovis
Clovis.east = Selma
Selma.north = Hanford
Hanford.west = Dinuba
Dinuba.south = Madera
Madera.west = Riverdale
Riverdale.east = "You have died"

player = Player(Fresno)

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
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
