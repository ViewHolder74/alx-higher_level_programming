#!/usr/bin/python3

# 0. If it's not tested it doesn't work.
# Run: python3 -m unittest discover tests

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


# Test Cases
class RectangleInstances(unittest.TestCase):
    """A class that defines instances of the Rectangle model"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rect.width)

    def test_width_setter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.width = 10
        self.assertEqual(10, rect.width)

    def test_height_getter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rect.height)

    def test_height_setter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.height = 10
        self.assertEqual(10, rect.height)

    def test_x_getter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rect.x)

    def test_x_setter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.x = 10
        self.assertEqual(10, rect.x)

    def test_y_getter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rect.y)

    def test_y_setter(self):
        rect = Rectangle(5, 7, 7, 5, 1)
        rect.y = 10
        self.assertEqual(10, rect.y)


# Test Cases
class WidthInstance(unittest.TestCase):
    """A class that defines instances for width attribute"""

    def test_width_is_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_is_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("3", 2)

    def test_width_is_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(4.5, 1)

    def test_width_is_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 2)

    def test_width_is_dictionary(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"w": 1, "h": 2}, 2)

    def test_width_is_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_width_is_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_width_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_width_is_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_width_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


# Test Case for height
class HeightInstances(unittest.TestCase):
    """A class that defines instances for height attribute"""

    def test_height_is_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_height_is_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_height_is_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 4.5)

    def test_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(4))

    def test_height_is_dictionary(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"w": 1, "h": 2})

    def test_height_is_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_height_is_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_height_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_height_is_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_height_is_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


# Test Cases for x
class XAttribute(unittest.TestCase):
    """A class that defines instances for x attribute"""

    def test_x_is_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_x_is_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3", 4)

    def test_x_is_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 9.5, 9)

    def test_x_is_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(4))

    def test_x_is_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"w": 1, "h": 2}, 2)

    def test_x_is_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_x_is_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_x_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2) 

    def test_x_is_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


# Test Cases for attribute
class YAttribute(unittest.TestCase):
    """A class that defines test cases for y attribute"""

    def test_y_is_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_y_is_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_y_is_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.3)

    def test_y_is_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(4))

    def test_y_is_dictionary(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"w": 1, "h": 2})

    def test_y_is_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_y_is_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_y_is_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_y_is_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

if __name__ == "__name__":
    unittest.main()
