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
    def __init__(self, name, description, damage, durability):
        super(Weapon, self).__init__(name)
        self.damage = damage
        self.description = description
        self.durability = durability


class Sword(Weapon):
    def __init__(self, name, description, damage, durability):
        super(Sword, self).__init__(name, description, damage, durability)


class IronS(Sword):
    def __init__(self, name, description, damage, durability=69):
        super(IronS, self).__init__(name, description, damage, durability)
        self.damage = damage
        self.durability = durability
        self.description = description


class DiamondS(Sword):
    def __init__(self, name, description, damage, durability=99):
        super(DiamondS, self).__init__(name, description, damage, durability)
        self.damage = damage
        self.durability = durability
        self.description = description


class WoodS(Sword):
    def __init__(self, name, description, damage, durability=11):
        super(WoodS, self).__init__(name, description, damage, durability)
        self.damage = damage
        self.durability = durability
        self.description = description


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)


class Leatherhel(Helmet):
    def __init__(self, name, description, durability=10):
        super(Leatherhel, self).__init__(name)
        self.durability = durability
        self.description = description


class Ironhel(Helmet):
    def __init__(self, name, description, durability=60):
        super(Ironhel, self).__init__(name)
        self.durability = durability
        self.description = description


class Diamondhel(Helmet):
    def __init__(self, name, description, durability=90):
        super(Diamondhel, self).__init__(name)
        self.durability = durability
        self.description = description


class Chainhel(Helmet):
    def __init__(self, name, description, durability=20):
        super(Chainhel, self).__init__(name)
        self.durability = durability
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


class DefaultH(Helmet):
    def __init__(self, name, durability=0):
        super(DefaultH, self).__init__(name)
        self.durability = durability


class DefaultC(Chestplate):
    def __init__(self, name, durability=0):
        super(DefaultC, self).__init__(name)
        self.durability = durability


class DefaultP(Pants):
    def __init__(self, name, durability=0):
        super(DefaultP, self).__init__(name)
        self.durability = durability


class DefaultB(Boots):
    def __init__(self, name, durability=0):
        super(DefaultB, self).__init__(name)
        self.durability = durability


class Hands(Sword):
    def __init__(self, name, description, damage, durability):
        super(Hands, self).__init__(name, description, damage, durability)
        self.damage = damage
        self.description = description


class Character(object):
    def __init__(self, name, health, weapon, helmet, chestplate, pants, boots):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.helm_armor = helmet
        self.ches_armor = chestplate
        self.pants_armor = pants
        self.boots_armor = boots

    def take_damage(self, damage):
        if damage < self.helm_armor.durability + self.ches_armor.durability \
                + self.pants_armor.durability \
                + self.boots_armor.durability:
            if self.helm_armor.durability == -30:
                print("You've been hit")
                self.health - damage

            if self.ches_armor.durability == -30:
                print("You've been hit")
                self.health - damage

            if self.pants_armor.durability == -30:
                print("You've been hit")
                self.health - damage

            if self.boots_armor.durability == -30:
                print("You've been hit")
                self.health - damage
                print("%s helmet =" % self.name, self.helm_armor.durability - damage)
                print("%s chest plate =" % self.name, self.ches_armor.durability - damage)
                print("%s pants =" % self.name, self.pants_armor.durability - damage)
                print("%s boots =" % self.name, self.boots_armor.durability - damage)
                print("No damage is done because of some fabulous armor!")
        if self.helm_armor.durability == -30:
            print("You've been hit")
            self.health - damage

        if self.ches_armor.durability == -30:
            print("You've been hit")
            self.health - damage

        if self.pants_armor.durability == -30:
            print("You've been hit")
            self.health - damage

        if self.boots_armor.durability == -30:
            print("You've been hit")
            self.health - damage

        if self.health < 0:
            self.health = 0
            print("%s has fallen, with left" % self.name)

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(Character):
    def __init__(self, starting_location):
        super(Player, self).__init__("Jemi", 100, Hands('hands', 'You have no weapon', 2, 0), DefaultH("hat"),
                                     DefaultC("shirt"),
                                     DefaultP("pants"),
                                     DefaultB("boots"))
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
Fresno = Room("Fresno", None, "You start in Fresno. Pick which weapon you want", None, None, None)
Kerman = Room("Kerman", None, "This is the second room there should be some armor", Fresno, None, None)
LA = Room("LA", Kerman, "Leads to another room", None, None, None)
SanFransisco = Room("SanFransisco", None, "Leads to another room", None, None, LA)
Washington = Room("Washington", None, "Leads to another room", None, SanFransisco, None)
Oregon = Room("Oregon", None, "Leads to another room", Washington, None, None)
Mexico = Room("Mexico", None, "Leads to another room", None, None, Oregon)
Antioch = Room("Antioch", Mexico, "Leads to another room", None, None, None)
DailyCity = Room("DailyCity", None, "Leads to another room", None, Antioch, None)
Clovis = Room("Clovis", None, "Leads to another room", None, None, DailyCity)
Selma = Room("Selma", None, "Leads to another room", None, Clovis, None)
Hanford = Room("Hanford", Selma, "Leads to another room", None, None, None)
Dinuba = Room("Dinuba", None, "Leads to another room", Hanford, None, None)
Madera = Room("Madera", None, "Leads to another room", None, None, Dinuba)
Riverdale = Room("Riverdale", "Leads to another room", Fresno, Madera, None, None)

# Defining
Fresno.west = Kerman
Fresno.north = Riverdale
Fresno.items.append(wood_sword)
Fresno.items.append(iron_sword)
Kerman.north = LA
Kerman.items.append(diamond_helmet)
Kerman.items.append(iron_chestplate)
LA.south = SanFransisco
LA.items.append(iron_boots)
LA.items.append(diamond_sword)
SanFransisco.east = Washington
SanFransisco.items.append(chain_boots)
SanFransisco.items.append(diamond_chestplate)
Washington.west = Oregon
Washington.items.append(chain_chestplate)
Washington.items.append(chain_boots)
Oregon.south = Mexico
Oregon.items.append(diamond_boots)
Oregon.items.append(iron_chestplate)
Oregon.items.append(diamond_pants)
Mexico.north = Antioch
Mexico.items.append(ogor)
Mexico.items.append(treasures)
Antioch.east = DailyCity
Antioch.items.append(ogor)
Antioch.items.append(Treasure2)
DailyCity.south = Clovis
Clovis.east = Selma
Selma.north = Hanford
Hanford.west = Dinuba
Hanford.items.append(treasures)
Dinuba.south = Madera
Madera.west = Riverdale
Riverdale.items.append(treasure)

jemi = Player(Fresno)

directions = ['north', 'south', 'east', 'west', 'pick up', 'drop', 'attack ogor']
short_directions = ['n', 's', 'e', 'w']
playing = True

# Controller
while playing:
    print(jemi.current_location.name)
    print(jemi.current_location.description)
    print("Jemi is in %s" % jemi.current_location.name)
    print("You're commands are n, e, s, w, pick up, drop")
    strength1 = jemi.helm_armor.durability + jemi.ches_armor.durability
    strength2 = jemi.pants_armor.durability + jemi.boots_armor.durability
    Overall = strength1 + strength2

    for item in jemi.current_location.items:
        print(item.name)
        if jemi.current_location == Mexico:
            print("There is an enemy in this room.")
            ogor.attack(jemi)
            jemi.attack(ogor)
            ogor.attack(jemi)
            jemi.attack(ogor)
            ogor.attack(jemi)
            if jemi.health == 0:
                print("Game Over. You have fallen to the nasty ogor......")
                quit(0)
            if ogor.health == 0:
                print("Ogor health = %s" % ogor.health)
                print("You have slain the nasty ogor. Continue")
                Mexico.items.remove(ogor)

    print("Jemi's helmet is the %s" % jemi.helm_armor.name)
    print("Jemi's chest plate is %s" % jemi.ches_armor.name)
    print("Jemi's pants is %s" % jemi.pants_armor.name)
    print("Jemi's shoes is %s" % jemi.boots_armor.name)
    print("Jemi's weapon is %s" % jemi.weapon.name)
    print("Your strength is %s" % Overall)
    print("Your power is %s" % jemi.weapon.damage)

    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command)
        command = directions[pos]

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
            if type(jemi.helm_armor) is DefaultH:
                if found_item in [diamond_helmet, chain_helmet, iron_helmet, leather_helmet]:
                    jemi.helm_armor = found_item

            if type(jemi.ches_armor) is DefaultC:
                if found_item in [diamond_chestplate, chain_chestplate, iron_chestplate, leather_chestplate]:
                    jemi.ches_armor = found_item

            if type(jemi.pants_armor) is DefaultP:
                if found_item in [diamond_pants, iron_pants, leather_pants, chain_pants]:
                    jemi.pants_armor = found_item

            if type(jemi.boots_armor) is DefaultB:
                if found_item in [diamond_boots, iron_boots, leather_boots, chain_boots]:
                    jemi.boots_armor = found_item

            if type(jemi.weapon) is Hands:
                if found_item in [wood_sword, diamond_sword, iron_sword]:
                    jemi.weapon = found_item

            jemi.inventory.append(found_item)
            jemi.current_location.items.remove(found_item)
            print("You picked up the %s" % found_item.name)
            print("Jemi's helmet is the %s" % jemi.helm_armor.name)
            print("Jemi's chest plate is %s" % jemi.ches_armor.name)
            print("Jemi's pants is %s" % jemi.pants_armor.name)
            print("Jemi's shoes is %s" % jemi.boots_armor.name)
            print("Jemi's weapon is %s" % jemi.weapon.name)
            print("Your power is %s" % jemi.weapon.damage)

            strength1 = jemi.helm_armor.durability + jemi.ches_armor.durability \
                        + jemi.pants_armor.durability + jemi.boots_armor.durability

            Overall = strength1
            print("Your strength is %s" % Overall)

    elif "drop" in command:
        item_name = command[5:]

        found_item = None
        # print(jemi.inventory)
        for item in jemi.inventory:
            if item.name == item_name:
                found_item = item

        if found_item is None:
            print("You don't have that")

        else:
            if jemi.helm_armor in [chain_helmet, diamond_helmet, iron_helmet, leather_helmet]:
                if found_item in [chain_helmet, diamond_helmet, iron_helmet, leather_helmet]:
                    jemi.helm_armor = DefaultH("hat")

            if jemi.ches_armor in [chain_chestplate, iron_chestplate, diamond_chestplate, leather_chestplate]:
                if found_item in [chain_chestplate, iron_chestplate, diamond_chestplate, leather_chestplate]:
                    jemi.ches_armor = DefaultC("shirt")

            if jemi.pants_armor in [chain_pants, iron_pants, diamond_pants, leather_pants]:
                if found_item in [chain_pants, iron_pants, diamond_pants, leather_pants]:
                    jemi.pants_armor = DefaultP("pants")

            if jemi.boots_armor in [chain_boots, iron_boots, diamond_boots, leather_boots]:
                if found_item in [chain_boots, iron_boots, diamond_boots, leather_boots]:
                    jemi.boots_armor = DefaultB("boots")

            if jemi.weapon in [wood_sword, iron_sword, diamond_sword]:
                if found_item in [wood_sword, iron_sword, diamond_sword]:
                    jemi.weapon = Hands('hands', 'You have no weapon', 2, 0)
            jemi.inventory.remove(found_item)
            jemi.current_location.items.append(found_item)
            print("You have dropped %s" % found_item.name)
            print("Jemi's helmet is %s" % jemi.helm_armor.name)
            print("Jemi's chest plate is %s" % jemi.ches_armor.name)
            print("Jemi's pants is %s" % jemi.pants_armor.name)
            print("Jemi's boots is %s" % jemi.boots_armor.name)
            print("Jemi's weapon is %s" % jemi.weapon.name)
            print("Your power is %s" % jemi.weapon.damage)
            strength1 = jemi.helm_armor.durability + jemi.ches_armor.durability
            strength2 = jemi.pants_armor.durability + jemi.boots_armor.durability
            Overall = strength1 + strength2
            print("Your strength is %s" % Overall)

    else:
        print("Not recognized.")
