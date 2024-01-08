#!/usr/bin/python3
"""Module of a rectangle class"""


class Rectangle:
    """Class representing a rectangle.

    Attributes:
        __height (int): The height of the rectangle.
        __width (int): The width of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional height and width.

        Args:
            height (int, optional): The height of the rectangle. Defaults to 0.
            width (int, optional): The width of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width > 0 and self.__height > 0:
            perimeter = 2 * (self.__width + self.__height)
        else:
            perimeter = 0
        return perimeter

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a representation of the rectangle.

        Returns:
            str: Representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"
