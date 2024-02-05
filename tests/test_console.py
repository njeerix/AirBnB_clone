#!/usr/bin/python3
"""
Unit tests for console using Mock from python standard library
"""

import unittest
from console import MyClass

class TestMyClass(unittest.TestCase):

    def test_add_positive_numbers(self):
        instance = MyClass()
        result = instance.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        instance = MyClass()
        result = instance.add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        instance = MyClass()
        result = instance.add(2, -3)
        self.assertEqual(result, -1)

    def test_multiply_numbers(self):
        instance = MyClass()
        result = instance.multiply(2, 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
