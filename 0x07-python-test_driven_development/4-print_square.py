#!/usr/bin/python3

"""A square-printing function."""

def print_square(size):
    """ A function that prints a square using #.
    Args:
        size: The size of the square input.
    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")