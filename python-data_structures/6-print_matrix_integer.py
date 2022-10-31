#!/usr/bin/python3
# A function that prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for col in i:
            print("{:d}".format(col), end=" " if col != i[-1] else "")
        print()
