# Resistor Colour Band Encoder/Decoder
**FILENAME:** README.md  
**VERSION:** 1  
**AUTHOR:** Reid Stasiuk  
**DATE:** 11/30/2025  
**SUMMARY:** The README file for the resistor colour band calculator

---

## DESCRIPTION

The resistor colour band calculator is a simple command-line program that can be used to decode a resistance value from a colour band representation or encode a colour band representation from a numerical resistance value. The encoder and decoder functions pull from a small (hard-coded) data structure, which represents the IEEE standard for 4-band and 5-band resistor colour codes.

To use the program, simply download the files from the repository and open the ResistorsMain file with Python. When a user runs the main file in a CLI, they will be prompted to choose whether they want to encode or decode a resistor, before they are asked for the required colour band or numerical data. The user can repeat as many times as they would like.

Resistance value in the following range are supported: 10Ω < R < 9.99GΩ
Tolerance percentages in the following list are supported: 0.05%, 0.10%, 0.25%, 0.50%, 1%, 2%, 5%, 10%

---

## RELEASE PACKAGE

1. Command Line Executable (`ResistorsMain.py`)
2. IEEE Resistor Code Database (`ColourBandDB`)
3. Encoder Function (`ColourBandEncoder.py`)
4. JSON data (`ColourBandDecoder.py`)
5. README file (`README.MD`)

---

## PROJECT FUNCTIONS

### `encode`  
**Desc:** Prompt user to enter a numercial resistance and tolerance. Outputs the 4-band and 5-band resistor encoding

### `decode`
**Desc:** Prompt user to enter a colour band encoding (4-band or 5-band). Outputs the numerical resistance and tolerance values

---

## DEPENDENCIES

None
