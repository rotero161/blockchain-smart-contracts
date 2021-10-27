"""
In this function we create a hash value of three characters for every string introduced
"""

# Import libraries
import numpy as np

def simpleHash(string):

    ## First position of the hash
    # Take the first character and its position in the ASCII code
    first_char = string[0]
    position_1 = ord(first_char)
    # If the ASCII code has two numbers, get the module division by 7 (the rest)
    if position_1 > 9:
        position_1 = position_1 % 7

    ## Second position of the hash
    # Take the last character and its position in the ASCII code
    last_char = string[-1]
    position_2 = ord(last_char)
    # If the ASCII code has two numbers, get the module division by 3 (the rest)
    if position_2 > 9:
        position_2 = position_2 % 3
    # Divide into 2 and round it
    position_2 = int(np.around(position_2 / 2))

    ## Third position of the hash
    # Take the first and last characters and concatenate them
    position_3 = first_char + last_char

    hash_value = str(position_1) + str(position_2) + str(position_3)

    return hash_value


print(simpleHash('Hola'))
print(simpleHash('Roberto'))
print(simpleHash('Miguel'))
print(simpleHash('Luis'))
print(simpleHash('Adrian'))