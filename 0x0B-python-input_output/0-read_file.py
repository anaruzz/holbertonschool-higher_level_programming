#!/usr/bin/python3
def read_file(filename=""):
    """
    function that reads a file and prints
    the content to output
    """
    for line in open(filename):
        print(line, end="")
