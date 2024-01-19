#!/usr/bin/python3
"""
Module Name: json_serializer
Description: This module provides a function to create a dictionary
             description suitable for JSON serialization from an object.
"""


def class_to_json(obj):
    """
    Return a dictionary description suitable for JSON serialization.

    :param obj: An instance of a class with serializable attributes.
    :return: A dictionary representing the serialized object.
    """
    attributes = vars(obj)
    serializable_attributes = {
        key: value for key, value in attributes.items() if is_serializable(value)
    }
    return serializable_attributes


def is_serializable(value):
    """
    Check if value is serializable (list, dictionary, string, integer, boolean)

    :param value: The value to check.
    :return: True if the value is serializable, False otherwise.
    """
    return (
        isinstance(value, (list, dict, str, int, bool)) or
        (isinstance(value, type) and value.__name__ == 'bool')
    )
