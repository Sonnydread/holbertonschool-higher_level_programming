#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for S in set(my_list):
        sum = sum + S
    return sum
