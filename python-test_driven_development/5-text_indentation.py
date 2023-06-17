#!/usr/bin/python3
"""a function that prints a text with 2 new lines"""


def text_indentation(text):

    if type(text) != str:
        raise TypeError("text must be a string")
    K = 0
    for S in text:
        if K == 1 and S == ' ':
            x = ""
        elif K == 1 and S != ' ':
            K = 0
            pass
        if S in ['.', '?', ':']:
            K = 1
            print(f"{S}\n\n", end='')
        else:
            print(S, end='')
