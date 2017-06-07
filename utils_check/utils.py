#!/usr/bin/python

''' This function verifies if a symbol_1 is prefix of a symbol_2
    @:parameter : Strings in a binary format: symbol_1, symbol_2
    @:return    : Boolean '''
def isPrefixOf(symbol_1, symbol_2):
    isPrefix = symbol_2.startswith(symbol_1);
    return isPrefix

''' This function gives the non-prefix between two symbols
    @:parameter : Strings in a binary format: symbol_1, symbol_2
    @:return    : String in a binary format with the difference between two symbols '''
def suffixPart(symbol_1, symbol_2):
    aux = symbol_2.split(symbol_1)
    return aux

