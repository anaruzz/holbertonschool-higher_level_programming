#!/usr/bin/python3
def read_file(filename=""):
    """
    function that reads a file and prints
    the content to output
    @filename: the name of the file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
