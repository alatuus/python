#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'romanizer' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def romanizer(numbers):
    # Write your code here
    units_dictionary = {
        "0" : '',
        "1" : 'I',
        "2" : 'II',
        "3" : 'III',
        "4" : 'IV',
        "5" : 'V',
        "6" : 'VI',
        "7" : 'VII',
        "8" : 'VIII',
        "9" : 'IX'
    }
    
    tens_dictionary = {
        "0" : "",
        "1" : "X",
        "2" : "XX",
        "3" : "XXX",
        "4" : "XL",
        "5" : "L",
        "6" : "LX",
        "7" : "LXX",
        "8" : "LXXX",
        "9" : "XC"
    }
    
    hundreds_dictionary = {
        "0" : "",
        "1" : "C",
        "2" : "CC",
        "3" : "CCC",
        "4" : "CD",
        "5" : "D",
        "6" : "DC",
        "7" : "DCC",
        "8" : "DCCC",
        "9" : "CM"
    }
    
    result = []
    
    for x in numbers:
        result_string = ""

        teste = str(x)

        if x == 1000:
            result_string = "M"
        elif len(teste) == 3:
            result_string = hundreds_dictionary[teste[0]] + tens_dictionary[teste[1]] + units_dictionary[teste[2]]
        elif len(teste) == 2:
            result_string =  tens_dictionary[teste[0]] + units_dictionary[teste[1]]
        elif len(teste) == 1:
            result_string =  units_dictionary[teste[0]]
        else:
            raise Exception(f"It must be between 1 and 1000, but it was {x}")
        
        result.append(result_string) 
        
    return result
        
def main():
    # Test cases
    test_numbers = [5, 246, 789, 1000]
    
    print(romanizer(test_numbers))
    # Expected output: ['XXXIX', 'CCXLVI', 'DCCLXXXIX', 'M']

if __name__ == "__main__":
    main()