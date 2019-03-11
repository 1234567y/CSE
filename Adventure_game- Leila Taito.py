class Room(object):
    def __init__(self, name, description=None, north=None, west=None, east=None, south=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.items = []


class Item(object):
    def __init__(self, name):
        self.name = name


class Treasure(Item):
    def __init__(self, name):
        super(Treasure, self).__init__(name)


class Treasure1(Treasure):
    def __init__(self, name, description):
        super(Treasure1, self).__init__(name)
        self.description = description


class Treasure2(Treasure):
    def __init__(self, name, description):
        super(Treasure2, self).__init__(name)
        self.description = description


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)


class IronS(Sword):
    def __init__(self, name, description, power=60, durability=69):
        super(IronS, self).__init__(name)
        self.power = power
        self.durability = durability
        self.description = description


class DiamondS(Sword):
    def __init__(self, name, description, power=90, durability=99, ):
        super(DiamondS, self).__init__(name)
        self.power = power
        self.durability = durability
        self.description = description


class WoodS(Sword):
    def __init__(self, name, description, power=10, durability=11):
        super(WoodS, self).__init__(name)
        self.power = power
        self.durability = durability
        self.description = description


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)


class Leatherhel(Helmet):
    def __init__(self, name, description, strength=10):
        super(Leatherhel, self).__init__(name)
        self.strength = strength
        self.description = description


class Ironhel(Helmet):
    def __init__(self, name, description, strength=60):
        super(Ironhel, self).__init__(name)
        self.strength = strength
        self.description = description


class Diamondhel(Helmet):
    def __init__(self, name, description, strength=90):
        super(Diamondhel, self).__init__(name)
        self.strength = strength
        self.description = description


class Chainhel(Helmet):
    def __init__(self, name, description, strength=20):
        super(Chainhel, self).__init__(name)
        self.strength = strength
        self.description = description


class Chestplate(Item):
    def __init__(self, name):
        super(Chestplate, self).__init__(name)


class Leatherches(Chestplate):
    def __init__(self, name, description, durability=10):
        super(Leatherches, self).__init__(name)
        self.durability = durability
        self.description = description


class Ironches(Chestplate):
    def __init__(self, name, description, durability=60):
        super(Ironches, self).__init__(name)
        self.durability = durability
        self.description = description


class Diamondches(Chestplate):
    def __init__(self, name, description, durability=90):
        super(Diamondches, self).__init__(name)
        self.durability = durability
        self.description = description


class Chainches(Chestplate):
    def __init__(self, name, description, durability=20):
        super(Chainches, self).__init__(name)
        self.durability = durability
        self.description = description


class Pants(Item):
    def __init__(self, name):
        super(Pants, self).__init__(name)


class DiamondP(Pants):
    def __init__(self, name, description, durability=90):
        super(DiamondP, self).__init__(name)
        self.durability = durability
        self.description = description


class LeatherP(Pants):
    def __init__(self, name, description, durability=10):
        super(LeatherP, self).__init__(name)
        self.durability = durability
        self.description = description


class IronP(Pants):
    def __init__(self, name, description, durability=60):
        super(IronP, self).__init__(name)
        self.durability = durability
        self.description = description


class ChainP(Pants):
    def __init__(self, name, description, durability=20):
        super(ChainP, self).__init__(name)
        self.durability = durability
        self.description = description


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)


class IronB(Boots):
    def __init__(self, name, description, durability=60):
        super(IronB, self).__init__(name)
        self.durability = durability
        self.description = description


class DiamondB(Boots):
    def __init__(self, name, description, durability=90):
        super(DiamondB, self).__init__(name)
        self.durability = durability
        self.description = description


class LeatherB(Boots):
    def __init__(self, name, description, durability=10):
        super(LeatherB, self).__init__(name)
        self.durability = durability
        self.description = description


class ChainB(Boots):
    def __init__(self, name, description, durability=20):
        super(ChainB, self).__init__(name)
        self.durability = durability
        self.description = description


class Potion(Item):
    def __init__(self, name, descripton):
        super(Potion, self).__init__(name)
        self.description = descripton

    def health(self):
        if command == "drink":
            self.health += 40


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


class Enemy(object):
    def __init__(self):
        self.health = 100
        self.inventory = [diamond_sword]
        self.current_location = SanFransisco.north


treasure = Treasure2("Treasure #2", "This is an item you need")
treasures = Treasure1("Treasure #1", "You also need this to win the game")
iron_sword = IronS("Iron Sword", "This is a sword")
diamond_sword = DiamondS("Diamond Sword", "This is the strongest sword you can get")
wood_sword = WoodS("Wood Sword", "This is the weakest sword you can get")
leather_helmet = Leatherhel("Leather Helmet", "This is the weakest helmet you can get")
chain_helmet = Chainhel("Chain Helmet", "This is a helmet")
diamond_helmet = Diamondhel("Diamond Helmet", "This is the strongest helmet you can get")
iron_helmet = Ironhel("Iron Helmet", "This is a helmet")
diamond_chestplate = Diamondches("Diamond Chest plate", "This is a chest plate")
iron_chestplate = Ironches("Iron Chest plate", "This is a chest plate")
leather_chestplate = Leatherches("Leather Chest plate", "This is a chest plate")
chain_chestplate = Chainches("Chain Chest plate", "This is a chest plate")
diamond_pants = DiamondP("Diamond Pants", "This is pants")
iron_pants = IronP("Iron Pants", "This is pants")
leather_pants = LeatherP("Leather Pants", "This is pants")
chain_pants = ChainP("Chain Pants", "This is pants")
diamond_boots = DiamondB("Diamond Boots", "This is boots")
iron_boots = IronB("Iron Boots", "This is boots")
chain_boots = ChainB("Chain Boots", "This is boots")
leather_boots = LeatherB("Leather Boots", "This is boots")
health_potion = Potion("Health Potion", "This is a health potion drink it to gain health")


Fresno = Room("Fresno", "Leads to another room", None, None, None, None)
Kerman = Room("Kerman", "Leads to another room", None, Fresno, None, None)
LA = Room("LA", "Leads to another room", Kerman, None, None, None)
SanFransisco = Room("SanFransisco", "Leads to another room", None, None, None, LA)
Washington = Room("Washington", "Leads to another room", None, None, SanFransisco, None)
Oregon = Room("Oregon", "Leads to another room", None, Washington, None, None)
Mexico = Room("Mexico", "Leads to another room", None, None, None, Oregon)
Antioch = Room("Antioch", "Leads to another room", Mexico, None, None, None)
DailyCity = Room("DailyCity", "Leads to another room", None, None, Antioch, None)
Clovis = Room("Clovis", "Leads to another room", None, None, None, DailyCity)
Selma = Room("Selma", "Leads to another room", None, None, Clovis, None)
Hanford = Room("Hanford", "Leads to another room", Selma, None, None, None)
Dinuba = Room("Dinuba", "Leads to another room", None, Hanford, None, None)
Madera = Room("Madera", "Leads to another room", None, None, None, Dinuba)
Riverdale = Room("Riverdale", "Leads to another room", Fresno, Madera, None, None)


Fresno.west = Kerman
Fresno.north = Riverdale
Fresno.items.append(wood_sword)
Fresno.items.append(iron_sword)
Kerman.north = LA
Kerman.items.append(diamond_helmet)
Kerman.items.append(leather_helmet)
LA.south = SanFransisco
LA.east = iron_boots
LA.west = diamond_sword
SanFransisco.east = Washington
SanFransisco.north = Enemy
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

player = Player(Fresno)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")
    if command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way.")
    elif command.lower() in ['q', 'quit', 'exit']:
            playing = False
    else:
        print("Command not recognized.")
