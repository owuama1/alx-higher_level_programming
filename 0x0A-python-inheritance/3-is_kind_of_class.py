#!/usr/bin/python3
"""
Module: class_check_module

provides a func to see if an obj is an instance
of a specified class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if the object is an instance of the specified class
    or its subclasses; otherwise, False.
    """
    return isinstance(obj, a_class)
