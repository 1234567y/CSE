class Room(object):
    def __init__(self, name, character=None, description=None, north=None, west=None, east=None, south=None):
        if character is None:
            character = []
        self.name = name
        self.character = character
        self.description = description
        self.items = []
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
    def __init__(self, name, description):
        super(Treasure1, self).__init__(name)
        self.description = description


class Treasure2(Treasure):
    def __init__(self, name, description):
        super(Treasure2, self).__init__(name)
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.description = description


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)


class IronS(Sword):
    def __init__(self, name, description, damage, durability=69):
        super(IronS, self).__init__(name)
        self.damage = damage
        self.durability = durability
        self.description = description


class DiamondS(Sword):
    def __init__(self, name, description, damage, durability=99, ):
        super(DiamondS, self).__init__(name)
        self.damage = damage
        self.durability = durability
        self.description = description


class WoodS(Sword):
    def __init__(self, name, description, damage, durability=11):
        super(WoodS, self).__init__(name)
        self.damage = damage
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


class Character(object):
    def __init__(self, name, health, weapon, helmet, chestplate, pants, boots):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = helmet
        self.armor = chestplate
        self.armor = pants
        self.armor = boots

    def take_damage(self, damage):
        if damage < self.armor.durability:
            print("No damage is done because of some fabulous armor!")
        else:
            self.health -= damage - self.armor.durability
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(Character):
    def __init__(self, starting_location):
        super(Player, self).__init__("Jemi", 100, None, chain_helmet, chain_chestplate, chain_pants, chain_boots)
        self.health = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        self.current_location = new_location

    def find_room(self, direction):
        return getattr(self.current_location, direction)


# Items
treasure = Treasure2("treasure #2", "This is an item you need")
treasures = Treasure1("treasure #1", "You also need this to win the game")
iron_sword = IronS("iron sword", "This is a sword", 60)
diamond_sword = DiamondS("diamond sword", "This is the strongest sword you can get", 90)
wood_sword = WoodS("wood sword", "This is the weakest sword you can get", 10)
leather_helmet = Leatherhel("leather helmet", "This is the weakest helmet you can get")
chain_helmet = Chainhel("chain helmet", "This is a helmet")
diamond_helmet = Diamondhel("diamond helmet", "This is the strongest helmet you can get")
iron_helmet = Ironhel("iron helmet", "This is a helmet")
diamond_chestplate = Diamondches("diamond chest plate", "This is a chest plate")
iron_chestplate = Ironches("iron chest plate", "This is a chest plate")
leather_chestplate = Leatherches("leather chest plate", "This is a chest plate")
chain_chestplate = Chainches("chain chest plate", "This is a chest plate")
diamond_pants = DiamondP("diamond pants", "This is pants")
iron_pants = IronP("iron pants", "This is pants")
leather_pants = LeatherP("leather pants", "This is pants")
chain_pants = ChainP("chain pants", "This is pants")
diamond_boots = DiamondB("diamond boots", "This is boots")
iron_boots = IronB("iron boots", "This is boots")
chain_boots = ChainB("chain boots", "This is boots")
leather_boots = LeatherB("leather boots", "This is boots")

# Character set up
ogor = Character("Ogor", 100, iron_sword, iron_helmet, iron_chestplate, iron_pants, iron_boots)

# Rooms
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

# Defining
Fresno.west = Kerman
Fresno.north = Riverdale
Fresno.items.append(wood_sword)
Fresno.items.append(iron_sword)
Kerman.north = LA
Kerman.items.append(diamond_helmet)
Kerman.items.append(leather_helmet)
LA.south = SanFransisco
LA.items.append(iron_boots)
LA.items.append(diamond_sword)
SanFransisco.east = Washington
SanFransisco.items.append(chain_boots)
SanFransisco.items.append(diamond_chestplate)
Washington.west = Oregon
Washington.items.append(chain_chestplate)
Oregon.south = Mexico
Oregon.items.append(diamond_boots)
Oregon.items.append(iron_chestplate)
Mexico.north = Antioch
Mexico.items.append(ogor)
Antioch.east = DailyCity
DailyCity.south = Clovis
Clovis.east = Selma
Selma.north = Hanford
Hanford.west = Dinuba
Hanford.items.append(treasures)
Dinuba.south = Madera
Madera.west = Riverdale
Riverdale.items.append(treasure)

jemi = Player(Fresno)

directions = ['north', 'south', 'east', 'west', 'pick up', 'attack orc', 'drop']

playing = True

# Controller
while playing:
    print(jemi.current_location.name)
    print(jemi.current_location.description)

    for item in jemi.current_location.items:
        print("Jemi is in %s" % jemi.current_location.name)
        print(item.name)
        if jemi.current_location == Mexico:
            print("An enemy is in this room fight or flee.")
            ogor.attack(jemi)

    command = input(">_")

    if command in directions:

        try:
            next_room = jemi.find_room(command)

            if next_room is None:
                raise KeyError
            jemi.move(next_room)

        except KeyError:
            print("Dead End")

    elif command.lower() in ['q', 'quit', 'exit']:
        playing = False

    elif "pick up " in command:
        item_name = command[8:]

        found_item = None
        for item in jemi.current_location.items:
            if item.name == item_name:
                found_item = item

        if found_item is None:
            print("I don't see one")
        else:
            jemi.inventory.append(found_item)
            jemi.current_location.items.remove(found_item)
            print("You pick up the %s" % found_item.name)

    elif "drop" in command:
        item_name = command[4:]

        for item in jemi.inventory:
            if item.name == item_name:
                found_item = item

        if item is None:
            print("You don't have that")

        else:
            print("You have dropped %s" % item)
            jemi.inventory.remove(item)
            jemi.current_location.items.append(item)
    else:
        print("Not recognized.")
