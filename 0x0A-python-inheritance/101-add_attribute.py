#!/usr/bin/python3
"""
Module: attribute_adder_module

This module provides a function for adding a new attribute to an object.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the new attribute is added.
        name: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute,
                   with the message "can't add new attribute."
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
