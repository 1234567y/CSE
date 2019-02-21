class Room(object):
    def __init__(self, name, description=None, north=None, west=None, east=None, south=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south


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
Riverdale.south = "Can't go there"
Riverdale.east = "You have died"
