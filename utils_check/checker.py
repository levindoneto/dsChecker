#!/usr/bin/python

# Library utilized
from utils_check import utils as check

''' This function is responsible for the dangling suffix checking of a code of symbols
    @:parameter : List with the symbols of a code
    @:return    : Boolean, true = code is uniquely decodable, false = code isn't uniquely decodable '''
def danglingSuffix(code, uniquely_decodable):
    this_uniquely_decodable = uniquely_decodable
    ''' Starting of the checking '''
    # All of the symbols in the code is checked with each other,
    # so an ordering of the symbols isn't needed
    print("THE LEN: ",len(code))
    for i in range(len(code)):
        for j in range(len(code)):
            sizeSymbol1 = len(code[i])
            sizeSymbol2 = len(code[j])
            equalSymbols = (code[i] == code[j])
            if (equalSymbols==True and i!= j):  # The comparison just matters if it's between 2 different symbols
                #print("IM HERE")
                this_uniquely_decodable = False

            elif (check.isPrefixOf(str(code[i]), str(code[j])) and i!=j):  # Code_i is prefix of code_j
                rest = check.suffixPart(str(code[i]), str(code[j]))
                # print("rest", rest)
                code.append(str(rest))
                print(code)

            else:
                pass
            j += 1

    return this_uniquely_decodable