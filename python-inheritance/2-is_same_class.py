#!/usr/bin/python3
"""function that returns true if the object is exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class
    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        True if the object is exactly an instance of the specified class, 
        otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
