#!/usr/bin/python

# Library utilized
from utils_check import utils as check

''' This function is responsible for the dangling suffix checking of a code of symbols
    @:parameter : List with the symbols of a code
    @:return    : Boolean, true = code is uniquely decodable, false = code isn't uniquely decodable '''
def danglingSuffix(code, list_pairs_indexes):
    i = 0
    j = 0
    global this_uniquely_decodable
    this_uniquely_decodable = True
    ''' Starting of the checking '''
    # All of the symbols in the code is checked with each other,
    # so an ordering of the symbols isn't needed
    while (i<len(code)):
        while (j < len(code)):
            print("CODE: ", code, ">>>> i:", i, "j:", j)
            print("LIST CMP: ", list_pairs_indexes)
            equalSymbols = (code[i] == code[j])
            alreadyCompared = check.alreadyCMP(i, j, list_pairs_indexes)
            print ("CMP: ", alreadyCompared)

            #if (alreadyCompared == False):
            #    list_pairs_indexes = check.addIndexesToList(i, j, list_pairs_indexes)
            #    print(list_pairs_indexes)
            list_pairs_indexes = check.addIndexesToList(i, j, list_pairs_indexes)  # Add the indexes already compared in a list for future verifications
            if (check.isPrefixOf(str(code[i]), str(code[j])) and i!=j and alreadyCompared == False):  # Code_i is prefix of code_j
                rest = check.suffixPart(str(code[i]), str(code[j]))
                code.append(str(rest)) # Add the non-prefix part to the last position of the list of symbols
                danglingSuffix(code, list_pairs_indexes) # Call the recursively the dangling function with the updated code list

            elif (equalSymbols==True and i!=j and alreadyCompared == False):  # The comparison just matters if it's between 2 different symbols
                this_uniquely_decodable = False
                continue
            j += 1
        i+=1

    return this_uniquely_decodable