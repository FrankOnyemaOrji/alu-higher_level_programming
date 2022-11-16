#!/usr/bin/python3
"""Defines a locked class."""


class lockedClass:
    """
    This class prevents the user from dynamically instantiating new attributes 
    for any new attribute but attributes called 'first_name'
    """

    __slots__ = ['first_name']
