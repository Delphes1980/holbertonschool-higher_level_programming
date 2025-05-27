#!/usr/bin/python3
"""
This module defines a class that inheritated from multiple classes
"""


class SwimMixin:
    """  A Mixin class that defines that the animal swims """

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """  A Mixin class that defines that the animal flies """

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):  # inheritance of the 2 Mixins
    """  A Mixin class that defines that the animal swims and flies """

    def roar(self):
        """ Prints what dragons do """
        print("The dragon roars!")

if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
