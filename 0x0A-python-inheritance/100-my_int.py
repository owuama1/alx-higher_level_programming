#!/usr/bin/python3
"""
Module: myint_module

This module defines the MyInt class.
"""


class MyInt(int):
    """
    A class representing MyInt, which inherits from int.

    MyInt has == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of the == operator.

        Args:
            other: The object to compare with.

        Returns:
            True if not equal; False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.

        Args:
            other: The object to compare with.

        Returns:
            True if equal; False otherwise.
        """
        return super().__eq__(other)
