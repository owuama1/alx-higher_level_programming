#!/usr/bin/python3
"""
Module: class_check_module

This module provides a function to check if an object is an instance of a
class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if the object is an instance of a class that inherited from
             the specified class; otherwise, False.
    """
    # Check if the object is an instance of the specified class
    if isinstance(obj, a_class):
        return True

    # Check if the object is an instance of a subclass of the specified class
    for subclass in obj.__class__.__bases__:
        if inherits_from(subclass, a_class):
            return True

    return False
