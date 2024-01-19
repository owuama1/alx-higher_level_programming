#!/usr/bin/python3
"""
Module Name: file_modifier
Description: This module provides a function to insert a line of text after
             each line containing a specific string in a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string.

    :param filename: The name of the file.
    :param search_string: The string to search for in each line.
    :param new_string: line of text to insert after lines with search string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
