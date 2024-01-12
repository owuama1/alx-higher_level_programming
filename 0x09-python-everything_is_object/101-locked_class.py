#!/usr/bin/python3

"""LockedClass - with restrictions on dynamic instance attribute creation."""


class LockedClass:
    """allows only 'first_name' as a dynamically created instance attribute."""
    __slots__ = ['first_name']

    def __init__(self):
        pass
