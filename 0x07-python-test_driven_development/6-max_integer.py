#!/usr/bin/python3

"""Finds the max integer in a list."""

def max_integer(list=[]):
    """ A function which finds and returns the highest integer in an input list.
        Return: None (if the list is empty).
    """

    if len(list) == 0:
        return None
    rslt = list[0]
    xx = 1
    while xx < len(list):
        if list[xx] > rslt:
            rslt = list[xx]
        xx += 1
    return