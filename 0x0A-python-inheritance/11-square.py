#!/usr/bin/python3
"""This module will define a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This will represent a square"""

    def __init__(self, size):
        """This will initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
