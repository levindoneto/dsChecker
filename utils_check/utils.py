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
        isPrefix = str(symbol_1).startswith(str(symbol_2))
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

    if (size_s1 < size_s2):
        for s in range(size_s1, size_s2):
            aux+=symbol_2[s]
    else:
        for s in range(size_s2, size_s1):
            aux+=symbol_1[s]
    print(aux, type(aux))
    return aux

''' This function is responsible for adding the two indexes in a list with two positions inside 
    the list of pairs of indexes already compared
    @:parameter : Integers index_1 and index_2, List of pairs of indexes already compared
    @:return    : NULL '''
def addIndexesToList(index_1, index_2, list_pairs_indexes):
    new_pair = [] # Auxiliar list which is always updated with new pairs of indexes already compared
    ''' Each pair is a list with two integers (indexes)'''
    new_pair.append(index_1)
    new_pair.append(index_2)

    list_pairs_indexes.append(new_pair)
    return True

''' This function verifies if two symbols of two different positions were already compared
    @:parameter : Integers index_1 and index_2, List of pairs of indexes already compared
    @:return    : Boolean, True: Already compared, False: They weren't compared yet'''
def alreadyCMP(index_1, index_2, list_pairs_indexes):
    for i in range(len(list_pairs_indexes)): # Accessing each pair of indexes (lists with len 2) individually
            fistConditionCMP = list_pairs_indexes[i][0] is index_1 and list_pairs_indexes[i][1] is index_2
            SecondConditionCMP = list_pairs_indexes[i][0] is index_1 and list_pairs_indexes[i][1] is index_2
            wereCMP = fistConditionCMP or SecondConditionCMP
    return wereCMP