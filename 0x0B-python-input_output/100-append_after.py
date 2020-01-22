#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    content = ""
    with open(filename, encoding='UTF-8') as f:
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(content)
