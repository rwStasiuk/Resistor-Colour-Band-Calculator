'''
FILENAME: ColourBandDB.py
VERSION: 1
AUTHOR: Reid Stasiuk
DATE: 11/24/2025
SUMMARY: The dictionary and list databases for the resistor colour band decoder script
'''

#standard resistor colour code database
colourDict = {
    "black":  {"digit": 0, "mult": 0,  "tol": None},
    "brown":  {"digit": 1, "mult": 1,  "tol": 1},
    "red":    {"digit": 2, "mult": 2,  "tol": 2},
    "orange": {"digit": 3, "mult": 3,  "tol": None},
    "yellow": {"digit": 4, "mult": 4,  "tol": None},
    "green":  {"digit": 5, "mult": 5,  "tol": 0.5},
    "blue":   {"digit": 6, "mult": 6,  "tol": 0.25},
    "violet": {"digit": 7, "mult": 7,  "tol": 0.1},
    "gray":   {"digit": 8, "mult": 8,  "tol": 0.05},
    "white":  {"digit": 9, "mult": 9,  "tol": None},
    "gold":   {"digit": None, "mult": -1, "tol": 5},
    "silver": {"digit": None, "mult": -2, "tol": 10},
}

#reverse lookup tables for O(1) time complexity
digitToColour = {v["digit"]: k for k, v in colourDict.items() if v["digit"] is not None}
multToColour  = {v["mult"]: k for k, v in colourDict.items()}
tolToColour   = {v["tol"]: k for k, v in colourDict.items() if v["tol"] is not None}
