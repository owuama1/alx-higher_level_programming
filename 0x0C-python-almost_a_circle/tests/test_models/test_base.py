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


class TestCreateMethod(unittest.TestCase):

    def test_create_with_attributes(self):
        obj = YourBaseClass.create(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_create_with_empty_attributes(self):
        obj = YourBaseClass.create()
        self.assertEqual(obj.id, 1)  # Assuming default id is 1
        self.assertEqual(obj.width, 1)  # Assuming default width is 1
        self.assertEqual(obj.height, 1)  # Assuming default height is 1
        self.assertEqual(obj.x, 0)  # Assuming default x is 0
        self.assertEqual(obj.y, 0)  # Assuming default y is 0

    def test_create_with_partial_attributes(self):
        obj = YourBaseClass.create(id=1, width=2)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        # Assuming default values for height, x, and y


if __name__ == '__main__':
    unittest.main()
