#!/usr/bin/python3
"""
Module Name: file_appender
Description: This module provides a function to append a string to the end of a
             text file in UTF-8 and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file in UTF-8 and return the number
    of characters added.

    :param filename: The name of the file to be appended.
    :param text: The string to be appended to the file.
    :return: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count
