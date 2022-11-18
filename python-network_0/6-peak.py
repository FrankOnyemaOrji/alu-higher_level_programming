#!/usr/bin/python3
"""
An element in the list is a peak if 
it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.
"""

def find_peak(list):
    """Find a peak in a list"""
    if list == []:
        return None

    def recusive(list, left=0, right=len(list) - 1):
        """helper recursive function"""

        mid = (left + right) // 2

        # check if mid is a peak
        if ((mid == 0 or list[mid - 1] <= list[mid]) and
            (mid == len(list) - 1 or list[mid + 1] <= list[mid])):
            return list[mid]
        
        # if mid is not a peak and its left neighbor is greater
        # than it, then left half must have a peak element
        if mid - 1 >= 0 and list[mid - 1] > list[mid]:
            return recusive(list, left, mid - 1)

        # if mid is not a peak and its right neighbor is greater
        # than it, then right half must have a peak element
        return recusive(list, mid + 1, right)

    return recusive(list)
