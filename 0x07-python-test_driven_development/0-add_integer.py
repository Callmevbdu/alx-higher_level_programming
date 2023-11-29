#!/usr/bin/python3

"""An integer addition function."""

def add_integer(a, b=98):
    """ Function that return the addition of a and b.
        Raises:
            TypeError: Whether a or b is a nor an integer or a float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))