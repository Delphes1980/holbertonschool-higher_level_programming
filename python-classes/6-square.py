#!/usr/bin/python3
"""

This module defines a class Square that represents a square shape.
"""


class Square:
    """
    A class that defines a square by its size and position

    Attributes:
    size (int): the size of the square's sides
    position (tuple): the position (horizontal & vertical offset) for printing

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square

        Note:
        __init__ method assign values to object properties
        size is a private instance attribute

        Args:
        size (int): The size of the square's sides (default 0)
        position (tuple): The position (horizontal, vertical)
        for display (default (0, 0))

        Raises:
        TypeError if size is not an integer or position is not a valid tuple
        ValueError is size is negative
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter for the size attribute
        The getter property retrieves the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for the size attribute.
        Ensures that the value is an integer >= 0
        """
        # Check if size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check is size is less than 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """ The getter for the position attribute
        The getter property retrieves the position in the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """The setter of the position attribute
        Ensures that the value is a 2 positive integers tuple
        """
        # Checks if position is a tuple
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Checks if position is a 2 integers tuple
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        # Checks if position is positive
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Note:
        area is a public instance method

        Returns:
        int: the area (size * size)

        """

        square_area = self.__size * self.__size
        return square_area

    def my_print(self):
        """
        Prints the square with the '#' character, respecting
        the position offset
        If size is 0, prints an empty line

        Note:
        area is a public instance method

        """

        if self.__size == 0:
            print()
            return
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
