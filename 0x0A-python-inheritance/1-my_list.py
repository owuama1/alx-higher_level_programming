#!/usr/bin/python3
"""
This module defines a class MyList that inherits list.

Public instance method:
    - def print_sorted(self): Prints the list in ascending sorted order.
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
