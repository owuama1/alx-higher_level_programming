#!/usr/bin/python3
"""
Module Name: file_writer
Description: This module provides a function to write a string to a text file
             in UTF-8 and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file in UTF-8 and return the number of characters
    written.

    :param filename: The name of the file to be written.
    :param text: The string to be written to the file.
    :return: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count
