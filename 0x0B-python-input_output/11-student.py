#!/usr/bin/python3
"""
Module Name: student
Description: This module defines a class Student with public instance
             attributes and methods for serialization and deserialization.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: A list of strings specifying which attributes to include.
                      If None, retrieve all attributes.
        :return: A dictionary representing the student instance.
        """
        if attrs is None:
            return vars(self)

        attributes = vars(self)
        filtered_attributes = {
            key: value for key, value in attributes.items() if key in attrs
        }
        return filtered_attributes

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.

        :param json: A dictionary representing the new values of attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
