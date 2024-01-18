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
    if issubclass(obj.__class__, a_class) and obj.__class__ != a_class:
        return True
    return False
