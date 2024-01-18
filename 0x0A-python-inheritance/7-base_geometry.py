#!/usr/bin/python3
"""
Module: geometry_module

This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing the base geometry.

    This class can be used as a base for more specific geometry-related
    classes in the future.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."

        This method should be overridden by subclasses to provide a
        specific implementation for calculating the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
