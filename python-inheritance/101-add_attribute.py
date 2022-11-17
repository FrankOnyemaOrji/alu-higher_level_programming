#!/usr/bin/python3
"""Module 101-add_attribute.py"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible
    Args:
        obj (object): the object to add the attribute to
        name (str): the name of the attribute
        value (object): the value of the attribute
    Raises:
        TypeError: if the object can't have new attributes
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
