#!/usr/bin/python3
"""Module 100-my_int.py"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Return the opposite of the == comparison"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return the opposite of the != comparison"""
        return int(self) == int(other)
