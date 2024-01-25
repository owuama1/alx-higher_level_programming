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

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance.

        Args:
            *args: Variable number of positional args in the ff order:
                   1st argument - id attribute
                   2nd argument - size attribute
                   3rd argument - x attribute
                   4th argument - y attribute
            **kwargs: Variable num of keyword args repr attr names and values.
        """
        if args:
            # If positional args are provided, use them and ignore **kwargs
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        elif kwargs:
            # If no positional arguments, use **kwargs
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: Formatted string with information about the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
