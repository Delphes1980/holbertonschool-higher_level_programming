#!/usr/bin/python3
"""
This module defines a method that reads a file (UTF8) and prints it to the
standard output
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf_8") as f:
        print(f.read(), end='')
