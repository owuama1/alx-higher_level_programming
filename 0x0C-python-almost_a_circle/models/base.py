#!/usr/bin/python3
"""
Module Name: base
Description: Contains the definition of the Base class.
"""

import json
import csv
import turtle


class Base:
    """
    Base class for other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int): Unique identifier for the base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances that inherit from Base.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List represented by the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set using the provided dictionary.

        Args:
            **dictionary: Dictionary containing attribute names and values.

        Returns:
            Base: Instance with attributes set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        screen = turtle.Screen()
        screen.bgcolor("white")

        turtle.speed(2)  # Adjust speed as needed

        # Draw Rectangles
        for rectangle in list_rectangles:
            Base.draw_rectangle(rectangle)

        # Draw Squares
        for square in list_squares:
            Base.draw_square(square)

        turtle.exitonclick()

    @staticmethod
    def draw_rectangle(rectangle):
        """Draw a Rectangle using Turtle graphics.

        Args:
            rectangle (Rectangle): Rectangle instance to be drawn.
        """
        turtle.penup()
        turtle.goto(rectangle.x, rectangle.y)
        turtle.pendown()
        turtle.color("blue")  # Adjust color as needed
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
        turtle.end_fill()

    @staticmethod
    def draw_square(square):
        """Draw a Square using Turtle graphics.

        Args:
            square (Square): Square instance to be drawn.
        """
        turtle.penup()
        turtle.goto(square.x, square.y)
        turtle.pendown()
        turtle.color("red")  # Adjust color as needed
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(square.size)
            turtle.left(90)
        turtle.end_fill()
