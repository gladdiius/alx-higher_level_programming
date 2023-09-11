#!/usr/bin/python3
"""defines a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square.

        Args:
            size(int): integer
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square."""
        return self.__size ** 2

