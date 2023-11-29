#!/usr/bin/python3

"""A text-indentation function."""

def text_indentation(text):
    """ A function which prints text with two new lines
        after each '.', '?', and ':'.
    Args:
        text: The input text.
    Raises:
        TypeError: If input isn't a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    xx = 0
    while xx < len(text) and text[xx] == ' ':
        xx += 1

    while xx < len(text):
        print(text[xx], end="")
        if text[xx] == "\n" or text[xx] in ".?:":
            if text[xx] in ".?:":
                print("\n")
            xx += 1
            while xx < len(text) and text[xx] == ' ':
                xx += 1
            continue
        xx += 1