#!/usr/bin/python3
"""
Module Name: file_reader
Description: This module provides a function to read a text file in UTF-8 and
             print its contents to stdout.
"""

def read_file(filename=""):
    """
    Read a text file in UTF-8 and print its contents to stdout.

    :param filename: The name of the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")

if __name__ == "__main__":
    pass

