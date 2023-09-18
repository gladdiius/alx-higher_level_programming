#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base
import sys


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

            Args:
                width (int): The width of the new Rectangle.
                height (int): The height of the new Rectangle.
                x (int): The x coordinate of the new Rectangle.
                y (int): The y coordinate of the new Rectangle.
                id (int): The identity of the new Rectangle.
            Raises:
                TypeError: If either of width or height is not an int.
                ValueError: If either of width or height <= 0.
                TypeError: If either of x or y is not an int.
                ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width
    @width.setter
    def width(self, width):
        self.validation('width', width)
        self.__width = width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height
    @height.setter
    def height(self, height):
        self.validation('height', height)
        self.__height = height

    @property
    def x(self):
        """Set/get the x of the Rectangle."""
        return self.__x
    @x.setter
    def x(self, x):
        self.validation('x', x)
        self.__x = x

    @property
    def y(self):
        """Set/get the y of the Rectangle."""
        return self.__y
    @y.setter
    def y(self, y):
        self.validation('y', y)
        self.__y = y

    def area(self):
        """returns the area of Rectangle."""
        return self.height * self.width

    def display(self):
        """display the Rectangle."""
        if self.__y:
            print("\n" * self.__y, end="")
        [print(' ' * self.x, '#' * self.width) for i in range(self.height)]
    
    def __str__(self):
        """returns the string representation of rectangle."""
        return f'{__class__.__name__} ({self.id}) {self.x}/{self.y} '\
                f'- {self.width}/{self.height}'

    def update(self, *args, **kwargs):
        """Update the Rectangle.

            Args:
                *args (ints): New attribute values.
                    - 1st argument represents id attribute
                    - 2nd argument represents width attribute
                    - 3rd argument represent height attribute
                    - 4th argument represents x attribute
                    - 5th argument represents y attribute
                **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for argname, arg in kwargs.items():
                if argname == "id":
                    self.id = arg
                elif argname == "width":
                    self.width = arg
                elif argname == "height":
                    self.height = arg
                elif argname == "x":
                    self.x = arg
                elif argname == "y":
                    self.y = arg

    def to_dictionary(self):
        """return dictionary representation of attributes"""
        return {'x': self.x, 
                'y': self.y, 
                'id': self.id, 
                'height': self.height, 
                'width': self.width
                }
    def validation(self, name, value):
        """Update the Rectangle.

            Args:
                value (any): value of the name
                name (str): name of the value
            Raises:
                TypeError: If either of width or height is not an int.
                ValueError: If either of width or height <= 0.
                TypeError: If either of x or y is not an int.
                ValueError: If either of x or y < 0.
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value < 0 and name in 'x y':
            raise ValueError(f'{name} must be >= 0')
        if value < 0 and name in 'width height':
            raise ValueError(f'{name} must be > 0')
