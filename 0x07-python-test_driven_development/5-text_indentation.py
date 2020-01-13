#!/usr/bin/python3
"""
Module that prints 2 lines instead of '?', '.' and ':'
text: text to check and print
"""
def text_indentation(text):
    """
    Print text with two lines
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    while i < (len(text)):
        print("{}".format(text[i]), end="")
        if text[i] in ['.', '?', ':']:
            while text[i] == ' ':
                i += 1
                continue
            print()
            print()
        i += 1
