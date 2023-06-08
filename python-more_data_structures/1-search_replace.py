#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for x in range(len(new)):
        if new[x] == search:
            new[x] = replace
    return new
