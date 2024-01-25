#!/usr/bin/python3
"""
Module Name: square
Description: Contains the definition of the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): Size of the square (width and height).
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            id (int): Unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Return a dictionary representation of the Square.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: Formatted string with information about the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
