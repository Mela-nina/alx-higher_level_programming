#!/usr/bin/python3
"""The writing of a docstring"""
import math


class MagicClass:
    """This sets up the magic"""

    def __init__(self, radius=0):
        """ The writing of another docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Another docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """A such docstring"""
        return 2 * math.pi * self.__radius
