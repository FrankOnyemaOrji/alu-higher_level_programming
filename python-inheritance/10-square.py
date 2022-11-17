#!/usr/bin/python3
"""Module 10-square.py"""
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """Square class"""

    def __init__(self, size):
        """Initialize a new Square
        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
