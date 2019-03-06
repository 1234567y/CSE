class Item(object):
    def __init__(self, name):
        self.name = name


class Treasure(Item):
    def __init__(self, name):
        super(Treasure, self).__init__(name)


class Treasures(Treasure):
    def __init__(self, name):
        super(Treasures, self).__init__(name)


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)


class Iron(Sword):
    def __init__(self, name, power=60):
        super(Iron, self).__init__(name)
        self.power = power


class Diamond(Sword):
    def __init__(self, name, power=90):
        super(Diamond, self).__init__(name)
        self.power = power


class Wood(Sword):
    def __init__(self, name, power=10):
        super(Wood, self).__init__(name)
        self.power = power


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)


class Leather(Helmet):
    def __init__(self, name, strength=10):
        super(Leather, self).__init__(name)
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