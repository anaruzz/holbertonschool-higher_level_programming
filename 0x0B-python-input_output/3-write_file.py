#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    function that writes a tring to a text file
    and returns number of characters written
    @filename: the name of the file
    @text: string to be written
    """
    with open(filename, mode="w", encoding='UTF-8') as f:
        n = f.write(text)
    return n
