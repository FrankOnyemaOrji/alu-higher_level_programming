#!/usr/bin/python3


# test_base.py
"""Defines unittests for models/base.py
Unittest for base.py:
    TestBase_instantiation
    TestBase_to_json_string
    TestBase_from_json_string
    TestBase_save_to_file
    TestBase_create
    TestBase_load_from_file
    TestBase_save_to_file_csv
    TestBase_load_from_file_csv
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Test cases for Base instantiation"""

    def test_starter(self):
        """Test for id=None"""
        base = Base()
        base1 = Base()
        base89 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base1.id, 2)
        self.assertEqual(base89.id, 3)

    def test_to_json_string(self):
        """Test for to_json_string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 89}]), '[{"id": 89}]')
        self.assertEqual(Base.to_json_string([{'id': 89}, str]))

    def test_from_json_string(self):
        """Test for from json string"""
        Base.__Base_nb_objects = 0
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(),
                             '[{"id": 1, "size": 1, "x": 0, "y": 0}]')
            Base.__Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(type(f.read()), str)

        Rectangle.save_to_file([Rectangle(1, 1)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(),
                    '[{"id": 1, "width": 1, '
                    '"height": 1, "x": 0, "y": 0}]')
