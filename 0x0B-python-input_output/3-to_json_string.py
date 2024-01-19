#!/usr/bin/python3
"""
Module Name: json_converter
Description: This module provides a function to return the JSON representation
             of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    :param my_obj: The object to be serialized to JSON.
    :return: A string representing the JSON serialization of the object.
    """
    return json.dumps(my_obj)
