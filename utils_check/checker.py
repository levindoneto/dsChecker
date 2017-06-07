#!/usr/bin/python

# Library utilized
from utils_check import utils as check

''' This function is responsible for the dangling suffix checking of a code of symbols
    @:parameter : List with the symbols of a code
    @:return    : Boolean, true = code is uniquely decodable, false = code isn't uniquely decodable '''
def danglingSuffix(code, uniquely_decodable):
    this_niquely_decodable = uniquely_decodable
    ''' Starting of the checking '''
    # All of the symbols in the code is checked with each other,
    # so an ordering of the symbols isn't needed
    for i in range(len(code)):
        for j in range(len(code)):
            if (code[i] == code[j] and i != j):  # The comparison just matters if it's between 2 different symbols
                this_niquely_decodable = False
            elif (check.isSuffixOf(code[i], code[j])):
                rest = check.nonSuffixPart(code[i], code[j])
                code.append(rest)
            else:
                pass
            j += 1

    return this_niquely_decodable