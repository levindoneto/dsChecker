#!/usr/bin/python

list = []

# Add values to the list of verification (manually)
print("________________________________________________________________")
print("| Insert the values (in a binary format)                       |")
print("| To add new values just press [ENTER] after each value added  |")
print("| Type 'stop' to stop the adding of values                     |")
print("|______________________________________________________________|\n")

value = input("> ")
list.append(value)
while value.strip() != 'stop':
    value = input("> ")
    if (value != "stop"):
        list.append(value)

print(list)