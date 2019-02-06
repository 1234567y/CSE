lives = 1
food = 0
Food = ["Pizza", "Fries", "Poison berry"]
playing = True
Cities = {
    "LA",
    "San Fransisco",
    "Washington",
    "Oregon",
    "Mexico",
    "Fresno",
    "Antioch",
    "Daily City",
    "Kerman",
    "Clovis",
    "Selma",
    "Hanford",
    "Dinuba",
    "Madera",
    "Riverdale"
}

areas = {
    'Fresno': {
        'NAME': "Desert",
        'DESCRIPTION': "This room will contain an object, look for it",
        'PATHS': {
            "N": "Gaston",
            "E": "LA",
            "S": "Back room",
            "W": "Kerman"

        }
    }
}


Moves = {
    "North": "N",
    "East": "E",
    "South": "S",
    "West": "W",
    "Pick up": "P",
    "Attack": "A"
}

while playing:
    command = input("_>")
    if command.lower()in ['q', 'quit', 'exit']:
        playing = False
    if command == Moves["North"]:
        print("You are in Fresno")
        print(areas["Fresno"]["DESCRIPTION"])


