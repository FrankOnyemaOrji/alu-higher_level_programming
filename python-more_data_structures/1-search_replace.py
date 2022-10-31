#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if col == search else col for col in my_list]
