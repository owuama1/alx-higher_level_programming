#!/usr/bin/python3
"""Defines a square class.

This module defines a Square class with a private instance attribute.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
