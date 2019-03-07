class Room(object):
    def __init__(self, name, description=None, north=None, west=None, east=None, south=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south


class Item(object):
    def __init__(self, name):
        self.name = name


class Treasure(Item):
    def __init__(self, name):
        super(Treasure, self).__init__(name)


class Treasure1(Treasure):
    def __init__(self, name):
        super(Treasure1, self).__init__(name)


class Treasure2(Treasure):
    def __init__(self, name):
        super(Treasure2, self).__init__(name)


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)


class IronS(Sword):
    def __init__(self, name, power=60, durability=69):
        super(IronS, self).__init__(name)
        self.power = power
        self.durability = durability


class DiamondS(Sword):
    def __init__(self, name, power=90, durability=99):
        super(DiamondS, self).__init__(name)
        self.power = power
        self.durability = durability


class WoodS(Sword):
    def __init__(self, name, power=10, durability=11):
        super(WoodS, self).__init__(name)
        self.power = power
        self.durability = durability


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)


class Leatherhel(Helmet):
    def __init__(self, name, strength=10):
        super(Leatherhel, self).__init__(name)
        self.strength = strength


class Ironhel(Helmet):
    def __init__(self, name, strength=60):
        super(Ironhel, self).__init__(name)
        self.strength = strength


class Diamondhel(Helmet):
    def __init__(self, name, strength=90):
        super(Diamondhel, self).__init__(name)
        self.strength = strength


class Chainhel(Helmet):
    def __init__(self, name, strength=20):
        super(Chainhel, self).__init__(name)
        self.strength = strength


class Chestplate(Item):
    def __init__(self, name):
        super(Chestplate, self).__init__(name)


class Leatherches(Chestplate):
    def __init__(self, name, durability=10):
        super(Leatherches, self).__init__(name)
        self.durability = durability


class Ironches(Chestplate):
    def __init__(self, name, durability=60):
        super(Ironches, self).__init__(name)
        self.durability = durability


class Diamondches(Chestplate):
    def __init__(self, name, durability=90):
        super(Diamondches, self).__init__(name)
        self.durability = durability


class Chainches(Chestplate):
    def __init__(self, name, durability=20):
        super(Chainches, self).__init__(name)
        self.durability = durability


class Pants(Item):
    def __init__(self, name):
        super(Pants, self).__init__(name)


class DiamondP(Pants):
    def __init__(self, name, durability=90):
        super(DiamondP, self).__init__(name)
        self.durability = durability


class LeatherP(Pants):
    def __init__(self, name, durability=10):
        super(LeatherP, self).__init__(name)
        self.durability = durability


class IronP(Pants):
    def __init__(self, name, durability=60):
        super(IronP, self).__init__(name)
        self.durability = durability


class ChainP(Pants):
    def __init__(self, name, durability=20):
        super(ChainP, self).__init__(name)
        self.durability = durability


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)


class IronB(Boots):
    def __init__(self, name, durability=60):
        super(IronB, self).__init__(name)
        self.durability = durability


class DiamondB(Boots):
    def __init__(self, name, durability=90):
        super(DiamondB, self).__init__(name)
        self.durability = durability


class LeatherB(Boots):
    def __init__(self, name, durability=10):
        super(LeatherB, self).__init__(name)
        self.durability = durability


class ChainB(Boots):
    def __init__(self, name, durability=20):
        super(ChainB, self).__init__(name)
        self.durability = durability


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


treasure = Treasure2("Treasure #2")
treasures = Treasure1("Treasure #1")
iron_sword = IronS("Iron Sword")
diamond_sword = DiamondS("Diamond Sword")
wood_sword = WoodS("Wood Sword")
leather_helmet = Leatherhel("Leather Helmet")
chain_helmet = Chainhel("Chain Helmet")
diamond_helmet = Diamondhel("Diamond Helmet")
iron_helmet = Ironhel("Iron Helmet")
diamond_chestplate = Diamondches("Diamond Chest plate")
iron_chestplate = Ironches("Iron Chest plate")
leather_chestplate = Leatherches("Leather Chest plate")
chain_chestplate = Chainches("Chain Chest plate")
diamond_pants = DiamondP("Diamond Pants")
iron_pants = IronP("Iron Pants")
leather_pants = LeatherP("Leather Pants")
chain_pants = ChainP("Chain Pants")
diamond_boots = DiamondB("Diamond Boots")
iron_boots = IronB("Iron Boots")
chain_boots = ChainB("Chain Boots")
leather_boots = LeatherB("Leather Boots")


Fresno = Room("Fresno", "One object in this room", None, None, None, None)
Kerman = Room("Kerman", "Leads to another room", None, Fresno, None, None)
LA = Room("LA", "Object here", Kerman, None, None, None)
SanFransisco = Room("SanFransisco", "Leads to another room", None, None, None, LA)
Washington = Room("Washington", "Leads to another room", None, None, SanFransisco, None)
Oregon = Room("Oregon", "Leads to another room", None, Washington, None, None)
Mexico = Room("Mexico", "Contains last object needed", None, None, None, Oregon)
Antioch = Room("Antioch", "Leads to another room", Mexico, None, None, None)
DailyCity = Room("DailyCity", "Leads to another room", None, None, Antioch, None)
Clovis = Room("Clovis", "Leads to another room", None, None, None, DailyCity)
Selma = Room("Selma", "Leads to another room", None, None, Clovis, None)
Hanford = Room("Hanford", "Leads to another room", Selma, None, None, None)
Dinuba = Room("Dinuba", "Leads to another room", None, Hanford, None, None)
Madera = Room("Madera", "Leads to another room", None, None, None, Dinuba)
Riverdale = Room("Riverdale", "This is where you can die.", Fresno, Madera, None, None)


Fresno.north = Riverdale
Fresno.west = Kerman
Fresno.east = wood_sword
Fresno.south = iron_sword
Kerman.north = LA
Kerman.east = diamond_helmet
Kerman.south = leather_helmet
LA.south = SanFransisco
LA.east = iron_boots
LA.west = diamond_sword
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
