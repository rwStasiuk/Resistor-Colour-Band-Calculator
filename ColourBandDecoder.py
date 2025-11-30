'''
FILENAME: ColourBandDecoder.py
VERSION: 1
AUTHOR: Reid Stasiuk
DATE: 11/24/2025
SUMMARY: The dictionary and list databases for the resistor colour band decoder script
'''

### RESISTOR COLOUR BAND DECODER ###
# decodes resistor size given colour bands 

import ColourBandDB as db

def decode():

    print("Legend:\n")
    print("black\nbrown\nred\norange\nyellow\ngreen\nblue\nviolet\ngray\nwhite\ngold\nsilver\n")

    while(1): #ask for the number of bands on resistor
        bandNumber = int(input("Enter the number of bands on your resistor (4|5): "))
        if bandNumber in (4, 5):
            break
        else: #if input is invalid, keep asking
            print("The number of bands can only be 4 or 5. Please try again")
            continue

    print("Begin entering band colours in order using the legend:")
    resistor = [] #list to collect the colours which are entered by the user
    for i in range(bandNumber): #collect the required number of resistor colors
        while(1): #ask for the color of each band
            colour = input(f"Enter band {str(i+1)} colour: ").lower().strip()
            if(colour in db.colourDict.keys()): #validate that the colour exists in the predefined dictionary
                resistor.append(colour)
                break
            else: #if input is invalid, keep asking
                print(f"Colour symbol '{colour}' not found. Please try again")
                
    #search through color dictionary to retrieve relevant data associated with each resistor band color
    num1 = db.colourDict[resistor[0]]["digit"]

    num2 = db.colourDict[resistor[1]]["digit"]

    num3 = db.colourDict[resistor[2]]["digit"] if bandNumber == 5 else 0

    multiplier = db.colourDict[resistor[3]]["mult"] if bandNumber == 5 else db.colourDict[resistor[2]]["mult"]

    tolerance = db.colourDict[resistor[4]]["tol"] if bandNumber == 5 else db.colourDict[resistor[3]]["tol"]

    #calculate resistance value using band colors
    x = (num1*10 + num2) if bandNumber == 4 else (num1*100 + num2*10 + num3)
    resistance = x*(10**multiplier)

    print("\n")
    if (tolerance is not None):
        print(f"Resistor: {resistance} +/- {tolerance}%\n")
    else:
        print(f"Resistor: {resistance} +/- UNK%\n")
