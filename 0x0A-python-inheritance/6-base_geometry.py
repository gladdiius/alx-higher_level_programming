#!/usr/bin/python3
"""defines baseclass geometry"""


class BaseGeometry:
    """represent base geometry."""

    def area(self):
        """raies exception not implemented."""
        raise Exception("area() is not implemented")
