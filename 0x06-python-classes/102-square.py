#!/usr/bin/python3
"""
Defines a square class.

This module defines a Square class with private instance attributes,
properties, and methods.
"""


class Square:
    """
    Defines a square.

    Attributes:
        size (int or float): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator."""
        return self.area() <= other.area()
