#!/usr/bin/python3
"""Define a square."""


class Square:
    """An empty class for Square.

        Args:
            size (int): width of square.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """Returns the area of a square."""
        return self.__size * self.__size
