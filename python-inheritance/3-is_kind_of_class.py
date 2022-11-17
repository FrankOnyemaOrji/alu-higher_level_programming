#!/usr/bin/python3
"""Module 3-is_kind_of_class.py"""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class
    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class, 
        otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False