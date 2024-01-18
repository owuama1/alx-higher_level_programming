#!/usr/bin/python3
"""
Module: geometry_module

This module defines the Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    This class inherits from Rectangle and adds specific behavior
    related to squares.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square (size * size).
        """
        return self.__size ** 2
