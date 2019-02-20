class Room(object):
    # This is constructor
    def __init__(self, name, east=None, north=None, south=None):  # declared stuff on right not declared stuff on left
        self.name = name
        self.east = east
        self.north = north
        self.south = south


# These are the instances of the rooms (Instantiation)

# Option 1 - Use the Variables, but fix later
R19A = Room("Mr.Wiebe's Room")
parking_lot = Room("The parking lot", None, R19A)

R19A.north = parking_lot
# Option 2 - Use Strings, but more difficult controller
R19A = Room("Mr. Wiebe's Room", 'parking_lot')
parking_lot = Room("The parking lot", None, R19A)
