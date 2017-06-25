#!/usr/bin/python

# Libraries utilized
from ui import menu as menu
from utils_check import checker as checkCode
from ui import result as showResult

code = [] # List of binary symbols of a code to be checked
list_pairs_indexes = [] # List with the already compared indexes | Format: [[i1,i2], [i1, i2],...], list with lists with 2 indexes

menu.showMenu()

# Add values to the list of verification (manually)
value = input("> ")
code.append(value)
while value.strip() != 's':
    value = input("> ")
    if (value != "s"):
        code.append(value)

result = checkCode.danglingSuffix(code, list_pairs_indexes)
showResult.result(result)

