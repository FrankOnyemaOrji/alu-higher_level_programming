#!/usr/bin/python3
"""Module 3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        if obj is an instance of a_class - True 
        otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
