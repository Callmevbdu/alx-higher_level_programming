#!/usr/bin/python3

"""A name-printing function."""

def say_my_name(first_name, last_name=""):
    """Function that prints a name.
    Args:
        first_name: The first string input.
        last_name: The second string input.
    Raises:
        TypeError: Whether first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
