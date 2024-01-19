#!/usr/bin/python3
"""
Module Name: json_loader
Description: This module
provides a function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    :param filename: The name of the JSON file to be loaded.
    :return: The object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
