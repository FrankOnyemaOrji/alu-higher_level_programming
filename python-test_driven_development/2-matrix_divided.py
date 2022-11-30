#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix (list of lists): matrix to divide
        div (int or float): divisor
    Raises:
        TypeError: if matrix is not a list of lists
        TypeError: if matrix contains non-numeric values
        TypeError: if matrix contains rows of different sizes
        ZeroDivisionError: if div is 0
    Returns:
        new_matrix (list of lists): divided matrix
    """
    if not isinstance(matrix, list) or not all (isinstance(row, list) for row in matrix) or not all(isinstance(ele, int) or isinstance(ele, float) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
