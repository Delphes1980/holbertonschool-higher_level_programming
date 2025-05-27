#!/usr/bin/python3
"""
This module defines a class that print a notification message every time an
item is added (using the append or extend methods) or removed (using the
remove or pop methods)
"""


class CountedIterator:
    """  A class that prints a message every time an item is added or removed
    """

    def __init__(self, iterable):
        """
        Initializes the CountedIterator.

        Args:
        iterable: The object to be iterated
        It must be an iterable(lists, tuples, dictionaries..)
        """
        self.iterator = iter(iterable)  # Initialize the iterator object
        self.count = 0  # Initialization of a counter

    def __iter__(self):
        """ Returns the iterator object itself """
        return self

    def __next__(self):
        """ Returns the next item """
        try:
            # Goes to the next item in the iterable
            count = next(self.iterator)
            type(self).count += 1  # Implementation of the counter
            return count
        except StopIteration:
            raise

    def get_count(self):
        """Returns the current number of iterated elements """
        return self.count
