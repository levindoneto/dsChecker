#!/usr/bin/python

''' This function provides the result of the checking to the user
    @:parameter : Boolean with the information about the code provided by the user
    @:return    : NULL '''
def result(uniquely_decodable):
    if (uniquely_decodable is not False):
        print ("The code is uniquely decodable")
    else:
        print("The code isn't uniquely decodable")