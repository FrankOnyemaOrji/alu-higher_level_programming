#!/usr/bin/python3
"""Defines a function reprensenting pascals triangle."""


def pasacal_triangle(n):
    """Represent Pascal's triangle of n.
    Returns a list of lists of integers representing the triangle
    """
    if n <= 0:
        return [] 

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        new = [1]
        for i in range(len(tri) - 1):
            new.append(tri[i] + tri[i + 1])
        new.append(1)
        triangle.append(new)
        return triangle
  