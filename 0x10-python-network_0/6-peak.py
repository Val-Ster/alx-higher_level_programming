#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element in the list.
    """
    if not list_of_integers:
        return None

    length = len(list_of_integers)

    if length == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[length - 1] >= list_of_integers[length - 2]:
        return list_of_integers[length - 1]

    for i in range(1, length - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]

    return None
