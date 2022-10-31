#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            print("{:d}".format(j), end=" " if i != matrix[-1] else "")
        print()
