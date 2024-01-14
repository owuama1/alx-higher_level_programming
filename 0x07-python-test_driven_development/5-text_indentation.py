#!/usr/bin/python3
"""
The defines a funct for text indentation. The funct takes a string as input
and prints the text with two new lines after each '.', '?', and ':' character.
"""


def text_indentation(text):
    """
    Prints the text with two new lines after each '.', '?', and ':' character.

    :param text: A string containing the input text.
    :type text: str
    :raises TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']

    current_line = ""
    for char in text:
        current_line += char
        if char in punctuation_chars:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
