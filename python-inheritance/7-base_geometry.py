#!/usr/bin/python3
"""Module 7-base_geometry.py"""


class BaseGeometry:
    """Represent a base geometry"""
    
    def area(self):
        """Public instance method that raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): name of the parameter
            value (int): value of the parameter
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
