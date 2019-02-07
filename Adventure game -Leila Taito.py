lives = 1
food = 0
Food = ["Pizza", "Fries", "Poison berry"]
City_map = {
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
        'NAME': "Fresno",
        'DESCRIPTION': "This room will contain an object, look for it",
        'PATHS': {
            'West': "Kerman"

        }
    },
    'Kerman': {
        'NAME': "Kerman",
        'DESCRIPTION': "Here you can get to LA",
        'PATHS': {
            'North': "LA"
        }
    },
    'LA': {
      'NAME': "LA",
      'DESCRIPTION': "From here you go to San Fransisco",
      'PATHS': {
            'South': "San Fransisco"
        }
    },
    'San Fransisco': {
        'NAME': "San Fransisco",
        'DESCRIPTION': "From here you go to Washington",
        'PATHS': {
            'East': "Washington"
        }
    },
    'Washington': {
        'NAME': "Washington",
        'DESCRIPTION': "From here you go to Oregon",
        'PATHS': {
            'East': "Oregon"
        }
    },
    'Oregon': {
        'NAME': "Oregon",
        'DESCRIPTION': "From here you go to Mexico",
        'PATHS': {
                'South': "Mexico"
            }
    },
    'Mexico': {
        'NAME': "Mexico",
        'DESCRIPTION': "From here you go to Antioch",
        'PATHS': {
            'North': "Antioch"
        }
    },
    }

Moves = {
    "North": "N",
    "East": "E",
    "South": "S",
    "West": "W",
    "Pick up": "P",
    "Attack": "A"
}
position = areas['Fresno']
playing = True
while playing:
    # print("Test")
    print(position["NAME"])
    command = input("_>")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in Moves:
        try:
            room_name = position["PATHS"][command]
            position = areas[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
