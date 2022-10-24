#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    i = dir(hidden_4)
    i.sort()
    for j in i:
        if j[:2] != "_":
            print(j)
