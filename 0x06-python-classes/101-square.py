#!/usr/bin/python3
"""This is my square module."""


class Square:
    """This defines a Square."""

    def __str__(self):
        """This teaches python to print the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ This initializes the square with this
        Args:
            size: This is a side of square
            position: Where the square is (coordinates)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is the property of the length of a side of square
        Raises:
            TypeError: If size is not an int.
            ValueError: If size is < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This sets the size of square
        Args:
            value: Size
        Raises:
                TypeError: If value is not int
                ValueError: If valie < 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """This is the property of the position of square
        Raises:
            TypeError: If value != tuple of 2 ints >= 0.
        Returns: Position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This sets the position
        Args:
            value: Where
        Raises:
                TypeError: If not tuple, ints, positive
        Returns: Position
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area of square
        Returns:
            size * size
        """
        return self.__size * self.__size

    def pos_print(self):
        """This returns the printed square with position"""
        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """This prints square."""
        print(self.pos_print(), end="")
