#!/usr/bin/python3
"""
It provides a func to get the list of available attr and methods of an obj

Usage:
    1. Import the module using: `import module_name`
    2. Call the function with an obj as an arg to get its attr and methods.
"""


def lookup(obj):
    """
    Returns a list containing attributes and methods of the given object.

    Parameters:
        obj (object): The object to inspect.

    Returns:
        list: A list containing attributes and methods of the object.
    """
    return dir(obj)
