#!/usr/bin/python3
"""
This module defines a class MyList that inherits list.

Public instance method:
    - def print_sorted(self): Prints the list in ascending sorted order.
"""


class MyList(list):
    """
    MyList class that inherits the built-in list class.

    Attributes:
        No additional attributes.

    Methods:
        - print_sorted(self): Prints the list in ascending sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
