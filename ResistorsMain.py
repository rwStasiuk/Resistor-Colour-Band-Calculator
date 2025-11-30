'''
FILENAME: ResistorsMain.py
VERSION: 1
AUTHOR: Reid Stasiuk
DATE: 11/24/2025
SUMMARY: The executable script for the resistor colour band encoder/decoder
'''

import ColourBandDecoder as cbd
import ColourBandEncoder as cbe

print("### RESISTOR COLOUR CODE CALCULATOR ###\n\n\n")

while(1): #loop while the user wants to continue encoding/decoding resistors
    print("Option 1: Decode a resistor (enter colour bands --> value)")
    print("Option 2: Encode a resistor (enter value --> colour bands)")

    opMode = None
    while opMode not in ("1", "2"): #poll for a valid operation mode
        opMode = input("Enter an option (1 | 2): ")
        if opMode.strip() == "":
            print("Input cannot be empty.")
        if opMode not in ("1", "2"):
            print(f"{opMode} is not a valid option. Please try again.")
    print("\n")
    
    if opMode == '1':
        try:
            cbd.decode() #decode a resistor and print string result
        except Exception as e:
            print(f"An error occurred while decoding: {e}")
            continue
    else:
        try:
            cbe.encode() #encode a resistor and print string result
        except Exception as e:
            print(f"An error occurred while decoding: {e}")
            continue
    
    #conditional repetition clause
    repeat = input("Would you like to encode/decode another resistor? (Y | N): ")
    if repeat.strip().lower() == 'y':
        print("\n")
        continue
    else:
        break

