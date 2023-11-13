#!/usr/bin/python3

# 0. If it's not tested it doesn't work
# Run: python3 -m unittest discover tests

import io
import sys
import unittest
from models.base import Base
from models.square import Square


# Test cases for square attribute
class SquareInstances(unittest.TestCase):
    """A class that defines instances of the Square model"""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


# Test Cases for size
class SizeAttribute(unittest.TestCase):
    """A class that defines instances for size attribute"""

    def test_size_is_(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_size_is_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("4")

    def test_size_is_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(4.5)

    def test_size_is_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(4))

    def test_size_is_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"w": 1, "h": 2}, 2)

    def test_size_is_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_size_is_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_size_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_size_is_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_size_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


# Teast case for x
class XAttribute(unittest.TestCase):
    """A class that defines instances for x attribute"""

    def test_x_is_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_x_is_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "3")

    def test_x_is_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_x_is_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_x_is_dictionary(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"w": 1, "h": 2}, 2)

    def test_x_is_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_x_is_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_x_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_x_is_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


# Test cases for y
class YAttribute(unittest.TestCase):
    """A class that defines instances for y attribute"""

    def test_y_is_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_y_is_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "2")

    def test_y_is_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_y_is_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_y_is_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"w": 1, "h": 2})

    def test_y_is_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_y_is_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_y_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_y_is_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)

if __name__ == "__name__":
    unittest.main()
