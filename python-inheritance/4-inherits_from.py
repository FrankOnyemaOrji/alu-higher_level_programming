#!/usr/bin/python3
"""Module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class
    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from the specified class, 
        otherwise False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False