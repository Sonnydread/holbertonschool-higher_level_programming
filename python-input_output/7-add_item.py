#!/usr/bin/python3
"""add all arguments, then save them"""


import sys
from os import path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    my_list = []
    if path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_to_json_file(my_list, "add_item.json")
