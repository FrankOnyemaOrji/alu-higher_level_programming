#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """check if an object is an instance of a class
    Args:
        obj (any): object to check
        a_class (type): The class to match the tyoe obj to.
        Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False
    """
    if type(obj) == a_class:
        return True
    return False
