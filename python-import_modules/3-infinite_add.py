#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    print("{:d}".format(sum(map(int, argv[1:]))))
