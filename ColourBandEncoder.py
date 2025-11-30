'''
FILENAME: ColourBandEncoder.py
VERSION: 1
AUTHOR: Reid Stasiuk
DATE: 11/24/2025
SUMMARY: Encodes a numeric resistance + tolerance into 4-band or 5-band resistor colour codes
'''

import ColourBandDB as db

def encode():

    while(1): #get resistance value and validate input
        resistance = input("Enter the desired resistance (neglect tolerance): ")
        try:
            int(resistance)
            break
        except ValueError: #if the input cannot be types casted to an integer, a ValueError is thrown
            print(f"'{resistance}' is not a valid resistance. Integers only.")
            continue

    if int(resistance) < 10: #calculator can't handle resistance values less than 10
        print("Resistances below 10Ω cannot be encoded using colour bands.")
        return

    while(1): #get tolerance value and validate input
        tolerance = input("Enter the desired tolerance as a percentage: ")
        try:
            float(tolerance) #allow decimals (e.g., 0.5%, 1%, 2%)
            break
        except ValueError: #if the input cannot be types casted to a float, a ValueError is thrown
            print(f"'{tolerance}' is not a valid tolerance. Integers and floats only.")
            continue
    
    digits = [int(d) for d in resistance]               #separate the digits in the resistance input

    num1, num2 = digits[0], digits[1]                   #first two digits always exist (values <10 were rejected)

    num3 = digits[2] if len(digits) > 2 else 0          #third digit used only for 5-band resistors

    mult5 = max(0, len(digits) - 3)                     #5-band multiplier = number of trailing zeros after 3 significant figures

    mult4 = mult5 + 1 if len(digits) > 2 else mult5     # 4-band multiplier = number of trailing zeros after 2 significant figures
                                                        # If 3 digits exist, multiplier shifts accordingly

    tol = round(float(tolerance), 1)                    #assign tolerance directly without clause

    #list of colours that make up the 5-band encoding
    #use reverse lookup tables to find colours
    encoding5Band = [
        db.digitToColour.get(num1),
        db.digitToColour.get(num2),
        db.digitToColour.get(num3),
        db.multToColour.get(mult5),
        db.tolToColour.get(tol)]

    #list of  colours that make up the 4-band encoding
    #use reverse lookup tables to find colours
    encoding4Band = [
        db.digitToColour.get(num1),
        db.digitToColour.get(num2),
        db.multToColour.get(mult4),
        db.tolToColour.get(tol)]


    print("\n4-Band Encoding:")
    if num3 == 0: #there can only be a 4-band encoding if only the first two signifigant figures of the resistance value are non-zero
        print(", ".join(encoding4Band))
    else:
        print("None")

    print("\n5-Band Encoding:")
    if len(digits) >= 3: #there can only be a 5-band encoding if the resistance value is at least 100 Ohms (3 digits)
        print(", ".join(encoding5Band))
    else:
        print("None")
    
    print("\n")