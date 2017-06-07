#!/usr/bin/python
from utils_check import utils as check

symbols = [] # List of binary symbols of a code to be checked
i = 0
j = 1
# Add values to the list of verification (manually)
print("________________________________________________________________")
print("| Insert the values (in a binary format)                       |")
print("| To add new values just press [ENTER] after each value added  |")
print("| Type 'stop' to stop the adding of values                     |")
print("|______________________________________________________________|\n")

value = input("> ")
symbols.append(value)
while value.strip() != 'stop':
    value = input("> ")
    if (value != "stop"):
        symbols.append(value)

''' Starting of the checking '''
# All of the symbols in the code is checked with each other,
# so an ordering of the symbols isn't needed
for i in range(len(symbols)):
    for j in range(len(symbols)):
        if(symbols[i]==symbols[j] and i!=j): # The comparison just matters if it's between 2 different symbols
            pass
        elif ( check.isSuffixOf(symbols[i], symbols[j]) ):
            rest = check.nonSuffixPart(symbols[i], symbols[j])
            symbols.append(rest)
        j+=1