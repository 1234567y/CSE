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
            'West': "Kerman",
            'North': "Riverdale"

        }
    },
    'Kerman': {
        'NAME': "Kerman",
        'DESCRIPTION': "Here you can get to LA",
        'PATHS': {
            'North': "LA",
            'West': "Fresno"
        }
    },
    'LA': {
      'NAME': "LA",
      'DESCRIPTION': "From here you go to San Fransisco",
      'PATHS': {
            'South': "San Fransisco",
            'North': "Kerman"
        }
    },
    'San Fransisco': {
        'NAME': "San Fransisco",
        'DESCRIPTION': "From here you go to Washington",
        'PATHS': {
            'East': "Washington",
            'South': "LA"
        }
    },
    'Washington': {
        'NAME': "Washington",
        'DESCRIPTION': "From here you go to Oregon",
        'PATHS': {
            'West': "Oregon",
            'East': "San Fransisco"
        }
    },
    'Oregon': {
        'NAME': "Oregon",
        'DESCRIPTION': "From here you go to Mexico",
        'PATHS': {
                'South': "Mexico",
                'West': "Washington"
            }
    },
    'Mexico': {
        'NAME': "Mexico",
        'DESCRIPTION': "From here you go to Antioch",
        'PATHS': {
            'North': "Antioch",
            'South': "Oregon"
        }
    },
    'Antioch': {
        'NAME': "Antioch",
        'DESCRIPTION': "From here you go to Daily City",
        'PATHS': {
            'East': "Daily City",
            'North': "Mexico"
        }
    },
    'Daily City': {
        'NAME': "Daily City",
        'DESCRIPTION': "From here you go to Clovis",
        'PATHS': {
            'South': "Clovis",
            'East': "Antioch"
        }
    },
    'Clovis': {
        'NAME': "Clovis",
        'DESCRIPTION': "From here you go to Selma",
        'PATHS': {
            'East': "Selma",
            'South': "Daily City"
        }
    },
    'Selma': {
        'NAME': "Selma",
        'DESCRIPTION': "From here you go to Hanford",
        'PATHS': {
            'North': "Hanford",
            'East': "Clovis"
        }
    },
    'Hanford': {
        'NAME': "Hanford",
        'DESCRIPTION': "From here you go to Dinuba",
        'PATHS': {
            'West': "Dinuba",
            'North': "Selma"
        }
    },
    'Dinuba': {
        'NAME': "Dinuba",
        'DESCRIPTION': "From here you go to Madera",
        'PATHS': {
            'South': "Madera",
            'West': "Hanford"
        }
    },
    'Madera': {
        'NAME': "Madera",
        'DESCRIPTION': "From here you go to Riverdale",
        'PATHS': {
            'West': "Riverdale",
            'South': "Dinuba"
        }
    },
    'Riverdale': {
        'NAME': "Riverdale",
        'DESCRIPTION': "From here you will go to Fresno",
        'PATHS': {
            'North': "Fresno",
            'West': "Madera"
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
