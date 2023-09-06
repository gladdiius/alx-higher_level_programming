#!/usr/bin/python3
"""define an attribute."""


class LockedClass(object):
    """lockes the name of the attribute."""
    __slots__ = ['first_name']
