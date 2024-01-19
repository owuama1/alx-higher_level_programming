#!/usr/bin/python3
"""
Module Name: json_converter
Description: This module provides a function to return a Python data structure
             represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Return a Python data structure represented by a JSON string.

    :param my_str: The JSON string to be converted.
    :return: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
