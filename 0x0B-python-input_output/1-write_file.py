#!/usr/bin/python3
"""This is the module that will define
a file-writing function."""


def write_file(filename="", text=""):
    """This will write a string to a UTF8 text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
