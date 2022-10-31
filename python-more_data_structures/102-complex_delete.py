#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary"""
    keys = list(a_dictionary.keys())
    for i in keys:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
