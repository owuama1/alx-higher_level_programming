#!/usr/bin/python3
"""
Module Name: student
Description: This module defines a class Student with public instance
             attributes and a method to retrieve a dictionary representation.
"""


class Student:
    """
    Class Name: Student
    Description: Represents a student with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance

        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        :return: A dictionary representing the student instance.
        """
        def is_serializable(value):
            """
            Check if a value is serializable (list, dict, str, int, bool).

            :param value: The value to check.
            :return: True if the value is serializable, False otherwise.
            """
            return (
                isinstance(value, (list, dict, str, int, bool)) or
                (isinstance(value, type) and value.__name__ == 'bool')
            )

        attributes = vars(self)
        serializable_attributes = {
            key: value for key, value in attributes.items() if is_serializable(value)
        }
        return serializable_attributes
