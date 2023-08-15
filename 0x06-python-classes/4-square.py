#!/usr/bin/python3
"""This is a module that defines a square """


class Square:
    """This is a class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: This represnets the size of the square defined
        Raises:
            TypeError: If size is not integer
            ValueError: If size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
