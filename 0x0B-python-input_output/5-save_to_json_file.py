#!/usr/bin/python3
"""
Module Name: json_saver
Description: This module provides a function to write an object to a text file
             using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    :param my_obj: The object to be serialized to JSON and saved.
    :param filename: The name of the file to save the JSON representation.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
