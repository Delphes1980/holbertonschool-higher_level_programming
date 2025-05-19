#!/usr/bin/python3
"""
    Module description: a module that contains a class called Square
that define a square

    Functions: class Square
"""


class Square:
    """ A class Square that defines a square

    """

    def __init__(self, size):
        """
            Instantiation of the size attribute

            Args:
            size: private instance attribute to control the size of the square
        """
        self.__size = size
