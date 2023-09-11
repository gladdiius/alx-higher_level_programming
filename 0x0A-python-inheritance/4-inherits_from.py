#!/usr/bin/python3
"""defines the is kind of class function"""


def inherits_from(obj, a_class):
    """ check if the object is an instance of a class
        Args:
            obj(any): object value
            a_class(any): class name
        Returns:
            If obj is an instance or inherited instance of a_class - True.
            Otherwise - False.
    """
    return isinstance(obj, a_class)
