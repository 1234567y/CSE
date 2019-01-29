states = {
    "CA": "California",
    "NJ": "New Jersey",
    "WI": "Wisconsin",
    "NY": "NewYork"
}

print(states["CA"])
print(states["WI"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000  # 39,500,000
    },
    "NJ": {
       "NAME": "New Jersey",
       "POPULATION": 9000000   # 9,000,000
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000  # 5,800,000
    },
    "NY": {
        "NAME": "New Jersey",
        "POPULATION": 19500000  # 19,500,000
    }
}

print(nested_dictionary["CA"])
print(nested_dictionary["CA"]["POPULATION"])
print(states["NY"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,  # 39,500,000
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angles"
        ]
    },
    "NJ": {
       "NAME": "New Jersey",
       "POPULATION": 9000000,   # 9,000,000
       "CITIES": [
           "Newark",
           "Trenton",
           "Princeton"
        ]
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000,  # 5,800,000
        "CITIES": [
            "",
            "",
            ""
        ]
    },
    "NY": {
        "NAME": "New Jersey",
        "POPULATION": 19500000,  # 19,500,000
        "CITIES": [
            "",
            "",
            ""
        ]
    }
}
