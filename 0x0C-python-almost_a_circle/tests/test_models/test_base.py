#!/usr/bin/python3
"""
Unit tests for models/base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_constructor_with_id(self):
        """
        Test constructor with a specified id.
        """
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_constructor_without_id(self):
        """
        Test constructor without a specified id.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_with_none_id(self):
        """
        Test constructor with None as id.
        """
        obj = Base(None)
        self.assertTrue(hasattr(obj, 'id'))

    def test_private_attribute(self):
        """
        Test access to private attribute __nb_objects.
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()
