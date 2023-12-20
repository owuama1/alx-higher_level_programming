#!/usr/bin/python3
"""
Defines a MagicClass that performs calculations based on a given radius.

This module defines a MagicClass with an initializer (__init__) to set the
radius attribute, and two methods (area and circumference) for calculating
the area and circumference based on the given radius.

"""

import math


class MagicClass:
    """
    Represents a MagicClass with radius-based calculations.

    Attributes:
        __radius (int or float): The radius of the MagicClass.

    Methods:
        __init__(self, radius=0): Initializes a new instance of MagicClass.
        area(self): Calculates and returns the area of the MagicClass.
        circumference(self): Calculates and returns the circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of MagicClass.

        Args:
            radius (int or float): The radius of the MagicClass.
        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the MagicClass.

        Returns:
            float: The calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the MagicClass.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
