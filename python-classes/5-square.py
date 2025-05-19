#!/usr/bin/python3
"""
    Module description: a module that contains a class called Square
that define a square

    Functions: class Square
"""


class Square:
    """
    A class Square that defines a square

    Properties:
    @property: retrieves the size of the square
    @size.setter: fixes the size of the square

    Attributes:
    def size(self)
    def size(self, value)
    def area(self)
    def my_print(self)

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

        self.size = size

    @property
    def size(self):
        """ The getter property retrieves the size of the square
        The setter property fixes the size of the square

        The setter checks if the size of the square is an integer
        and if it's less than 0
        """

        return self.__size

    @size.setter
    def size(self, value):
        # Check if size is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check is size is less than 0
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Returns the current square area

        Note:
        area is a public instance method

        Attributes:
        square_area (int): the area of the square
        size (int): the size of the square

        Returns:
        the current square area

        """

        square_area = self.__size * self.size
        return square_area

    def my_print(self):
        """
        prints in stdout the square with the character #

        Note:
        area is a public instance method

        Attributes:
        None

        Returns:
        the square printed with the character #

        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#", end='')
                for j in range(self.__size - 1):
                    print("#", end='')
                print()
