#!/usr/bin/python3
"""This defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is the class that represents a
    rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """This will intialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """This will return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This will return the print() and
        str() representation of a Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
