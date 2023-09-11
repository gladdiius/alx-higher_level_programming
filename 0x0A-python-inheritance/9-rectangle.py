#!/usr/bin/python3
"""define class rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the height"""
        return self.__width * self.__height

    def __str__(self):
        """prints the area of the rectangle."""
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
