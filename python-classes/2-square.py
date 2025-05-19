#!/usr/bin/python3
"""
    Module description: a module that contains a class called Square
that define a square

    Functions: class Square
"""


class Square:
    """ A class Square that defines a square

    """


    def __init__(self, size=0):
        """
        Instantiation of the size attribute

            Note:
            __init__ method assign values to object properties
            size is a private instance attribute

            Args:
            size (int): size of the square

            Attributes:
            size (int): size of the square

            Returns:
            the size of the square

            Raises:
            TypeError if size is not an integer
            ValueError is size is less than 0

        """

        # Check if size is an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check is size is less than 0
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
