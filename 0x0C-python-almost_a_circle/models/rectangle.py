#!/usr/bin/python3
"""
Module Name: rectangle
Description: Contains the definition of the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance using '#' characters.
        Takes care of x and y coordinates.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.

        Returns:
            str: Formatted string with information about the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}"
                "/{}".format(self.id, self.__x, self.__y,
                             self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args: Variable num of positional args.
            If provided, **kwargs is ignored.
            **kwargs: Variable number of keyword arguments
            representing attribute names and values.
        """
        if args:
            # If positional args are provided, use them and ignore **kwargs
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.y = args[4] if len(args) >= 5 else self.y
        else:
            # If no positional arguments, use **kwargs
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
