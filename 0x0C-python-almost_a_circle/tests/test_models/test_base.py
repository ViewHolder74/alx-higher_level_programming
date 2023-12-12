#!/usr/bin/python3

# 0. If it's not tested it doesn't work
# Run: python3 -m unittest discover tests

import os
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


# Base Model Instances test
class ModelInstances(unittest.TestCase):
    """A class to test instances of Base arguments"""

    def test_no_arg(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_four_bases(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        obj4 = Base()
        self.assertEqual(obj1.id, obj4.id - 3)

    def test_id_None(self):
        obj1 = Base(None)
        obj2 = Base(None)
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_unique_id(self):
        self.assertEqual(3, Base(3).id)

    def test_nb_instances_after_passed_id(self):
        obj1 = Base()
        obj2 = Base(3)
        obj3 = Base()
        self.assertEqual(obj1.id, obj3.id - 1)

    def test_id(self):
        obj = Base(3)
        obj.id = 6
        self.assertEqual(6, obj.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(3).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(7.8, Base(7.8).id)

    def test_complex_id(self):
        self.assertEqual(complex(7), Base(complex(7)).id)

    def test_dictionary_id(self):
        self.assertEqual({"width": 7, "height": 10},
                Base({"width": 7, "height": 10}).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
