#!/usr/bin/python

''' This function verifies if a symbol_1 is prefix of a symbol_2 or the opposite
    @:parameter : Strings in a binary format: symbol_1, symbol_2
    @:return    : Boolean '''
def isPrefixOf(symbol_1, symbol_2):
    len_s1 = len(symbol_1) # The 1st position of symbol_2 that is different from the suffix is in the position of the size of the symbol_1
    len_s2 = len(symbol_2)

    if (len_s1 < len_s2):
        isPrefix = str(symbol_2).startswith(str(symbol_1))
    else:
        isPrefix = str(symbol_2).startswith(str(symbol_1))
    return isPrefix

''' This function gives the non-prefix between two symbols
    @:parameter : Strings in a binary format: symbol_1, symbol_2
    @:return    : String in a binary format with the difference between two symbols '''
def suffixPart(symbol_1, symbol_2):
    # Here it can be assumed that symbol_1 has lower size than symbol_2
    aux = "" # String with the different part between symbol_1 and symbol_2
    symbol_1 = str(symbol_1)
    symbol_2 = str(symbol_2)

    size_s1 = len(symbol_1) # The 1st position of symbol_2 that is different from the suffix is in the position of the size of the symbol_1
    size_s2 = len(symbol_2)
    for s in range(size_s1, size_s2):
        aux+=symbol_2[s]
    print(aux, type(aux))
    return aux

