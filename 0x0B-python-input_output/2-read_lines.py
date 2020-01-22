#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines from a
    file and prints them to stdout
    @filename: the name of the file
    @nb_lines: number of lines
    """
    with open(filename) as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                for line in f:
                    print(line, end="")
        else:
            for line in f:
                print(line, end="")
