"""Module for adding two integers.
This module provides a function, add_integer, that adds two integers.
includes a docstring describing the purpose, usage, and behavior of the module.

"""


def add_integer(a, b=98):
    """Adds two integers.
    a, b as args and b b is 98 by default. a and b are floats or integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
