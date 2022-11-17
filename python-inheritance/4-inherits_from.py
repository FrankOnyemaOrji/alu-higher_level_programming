#!/usr/bin/python3
"""Module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """check if an object is an inherited instance of a class.
    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        if obj is an instance of a_class - True
        otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
