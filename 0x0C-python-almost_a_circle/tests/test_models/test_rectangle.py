#!/usr/bin/python3
"""
Unit tests for models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_constructor_with_valid_values(self):
        """
        Test constructor with valid values.
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_constructor_with_default_values(self):
        """
        Test constructor with default values.
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertTrue(hasattr(rect, 'id'))

    def test_setters_with_valid_values(self):
        """
        Test setters with valid values.
        """
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.width = 7
        rect.height = 8
        rect.x = 2
        rect.y = 3
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_setters_with_invalid_values(self):
        """
        Test setters with invalid values.
        """
        rect = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(ValueError):
            rect.width = -1
        with self.assertRaises(ValueError):
            rect.height = 0
        with self.assertRaises(ValueError):
            rect.x = -2
        with self.assertRaises(ValueError):
            rect.y = -3


if __name__ == '__main__':
    unittest.main()
