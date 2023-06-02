#!/usr/bin/python3
for x in range(0, 8):
    for s in range(x, 10):
        if x < s:
            print("{}{}, ".format(x, s), end="")
print("89")
