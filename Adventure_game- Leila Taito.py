class Room(object):
    def __init__(self, name, description=None, north=None, west=None, east=None, south=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south


Fresno = Room("This room will lead to Kerman and Riverdale")
Kerman = Room("This will lead to another room", None, Fresno)
Fresno.west = Kerman

