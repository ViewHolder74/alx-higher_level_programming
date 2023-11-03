#!/usr/bin/python3
"""5. Max integer - Unittest"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class that defines tests for maximum integer in list"""

    def test_unsigned(self):
        """Function to test for unsigned integers in normal list"""

        self.assertEqual(max_integer([7, -9, 10, 8]), 10)

    def test_empty(self):
        """Function to test an empty list"""

        self.assertEqual(max_integer([]), None)

    def test_repeated(self):
        """Function to test repeated integers"""

        self.assertEqual(max_integer([5, 1, 8, 8]), 8)

    def test_float(self):
        """Function to test floating point values"""

        self.assertEqual(max_integer([7.9, 0.6]), 7.9)

    def test_negative(self):
        """Function to test negative numbers in list"""

        self.assertEqual(max_integer([-13, -45, -21, -1]), -1)

    def test_string(self):
        """Function to test list with strings"""

        with self.assertRaises(TypeError):
            max_integer([9, '8'])

    def test_tuple(self):
        """Function to test list with tuple element"""

        with self.assertRaises(TypeError):
            max_integer([16, (1, 7)])

    def test_dictionary(self):
        """Function to test list with dictionary element"""

        with self.assertRaises(KeyError):
            max_integer({'height': 10, 'width': 5})

    def test_number(self):
        """Function to test single integer not in list"""

        with self.assertRaises(TypeError):
            max_integer(1)
