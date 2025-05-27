#!/usr/bin/python3
"""
This module defines an abstract class Animal
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """  An abstract class Animal """
    @abstractmethod
    def sound(self):
        """
        Return the sound of an animal
        """
        pass


class Dog(Animal):
    """  A class Dog that inherits from Animal"""
    def sound(self):
        """
        Return the sound of the object Dog
        """
        return "Bark"


class Cat(Animal):
    """  A class Dog that inherits from Animal"""
    def sound(self):
        """
        Return the sound of the object Cat
        """
        return "Meow"
