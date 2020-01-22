#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    function that appends a text to a file
    @filename: the path of the file
    @text: text to be added
    """
    with open(filename, mode="a", encoding='UTF-8') as f:
        n = f.write(text)
    return n
