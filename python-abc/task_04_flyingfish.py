#!/usr/bin/python3
"""
This module defines a class that inheritated from multiple classes
"""


class Fish:
    """  A class that defines an animal Fish """

    def swim(self):
        """ Prints what fish do """
        print("The fish is swimming")

    def habitat(self):
        """ Prints where fish live """
        print("The fish lives in water")


class Bird:
    """  A class that defines an animal Bird """

    def fly(self):
        """ Prints what birds do """
        print("The bird is flying")

    def habitat(self):
        """ Prints where birds live """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """  A class that defines a new kind of animal inheritated
    from Fish and Bird classes """

    def fly(self):
        """ Prints what the new animal does """
        print("The flying fish is soaring!")

    def swim(self):
        """ Prints what the nwe animal does """
        print("The flying fish is swimming!")

    def habitat(self):
        """ Prints where the new animal lives """
        print("The flying fish lives both in water and the sky!")
