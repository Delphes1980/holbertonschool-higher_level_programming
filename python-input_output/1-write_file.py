#!/usr/bin/python3
"""
This module defines a method that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file and returns the number
    of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
