#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines from a
    file and prints them to stdout
    @filename: the name of the file
    @nb_lines: number of lines
    """
    lines_read = 0
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            if lines_read < nb_lines or nb_lines <= 0:
                print(line, end="")
