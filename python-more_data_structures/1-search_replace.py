#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for xs in range(len(new)):
        if new[xs] == search:
            new[xs] = replace
    return new
