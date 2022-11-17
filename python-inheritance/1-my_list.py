#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Represent a MyList object"""

    def print_sorted(self):
        """Print the list, but sorted (ascending sort)"""
        print(sorted(self))
