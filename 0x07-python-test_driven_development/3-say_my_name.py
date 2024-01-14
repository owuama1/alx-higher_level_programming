"""
Module: my_name_printer

This module provides a function to print a formatted name statement.

"""

def say_my_name(first_name, last_name=""):
    """
    Prints the statement "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Raises:
        TypeError: If either first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + " " + last_name
    print("My name is " + full_name)
