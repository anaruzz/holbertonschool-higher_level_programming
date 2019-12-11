#!/usr/bin/python3
def uppercase(str):
    for c in range(0, len(str)):
        if ord(c) in range(97, 123):
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
    print()
