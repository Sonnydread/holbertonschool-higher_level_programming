#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for M in b_dictionary:
        b_dictionary[M] = b_dictionary[M] * 2
    return b_dictionary
