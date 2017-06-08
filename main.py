#!/usr/bin/python

# Libraries utilized
from ui import menu as menu
from utils_check import checker as checkCode
from ui import result as showResult

code = [] # List of binary symbols of a code to be checked
i = 0
j = 1
uniquely_decodable = True

menu.showMenu()

# Add values to the list of verification (manually)
value = input("> ")
code.append(value)
while value.strip() != 's':
    value = input("> ")
    if (value != "s"):
        code.append(value)

result = checkCode.danglingSuffix(code, uniquely_decodable)
showResult.result(result)

