#!/usr/bin/python3
"""Unittest for Square class"""
import os
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square



class TestSquare_instantiation(unittest.TestCase):
    """Unit tests for Square class instantiation"""

    def test_instance(self):
        """Test for instantiation"""
        Base.__Base__nb_objects = 0
        s1 = Square(10)
        s2 = Square(2, 12)
        s3 = Square(10, 0, 12)
        s4 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 1)

        with self.assertRaises(ValueError, msg="size must be > 0"):
            Square(-10)

        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square("10")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(10, "0")

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(10, 0, "12")

        with self.assertRaises(TypeError, msg="size must be an integer"):
            Square(10.5)

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(10, 0.5)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(10, 0, 12.5)

    def test_area(self):
        """Test for area"""
        a1 = Square(3)
        self.assertEqual(a1.area(), 9)

    def test__str__(self):
        """Test for __str__"""
        s1 = Square(4, 2, 1, 12)
        self.assertEqual(s1.__str__(), "[Square] (12) 2/1 - 4")

    def test_display(self):
        """Test for display"""
        s1 = Square(4)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            s1.display()
            self.assertEqual(fakeOutput.getvalue(), "##\n##\n")
        
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            s2.display()
            self.assertEqual(fakeOutput.getvalue(), "  ##\n  ##\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            s3.display()
            self.assertEqual(fakeOutput.getvalue(), "\n\n\n ###\n ###\n ###\n")

    def test_to_dictionary(self):
        """Test for dictionary"""
        d1 = Square(2)
        d2 = Square(2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            d1.display()
            self.assertEqual(fakeOutput.getvalue(), "##\n##\n")

        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            d2.display()
            self.assertEqual(fakeOutput.getvalue(), "  ##\n  ##\n")

    def test_update(self):
        """Test for updates"""
        Base.___Base__nb_objects = 0
        u1 = Square(10)
        u1.update()
        self.assertEqual(u1.id, 1)

        u1.update(89)
        self.assertEqual(u1.id, 89)

        u1.update(89, 2)
        self.assertEqual(u1.size, 2)
        self.assertEqual(u1.id, 89)

        u1.update(89, 2, 3)
        self.assertEqual(u1.size, 2)
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.x, 3)

        u1.update(89, 2, 3, 4)
        self.assertEqual(u1.size, 2)
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.x, 3)
        self.assertEqual(u1.y, 4)

        u1.update(**{'id': 89})
        self.assertEqual(u1.id, 89)

        u1.update(**{'id': 89, 'size': 2})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.size, 2)

        u1.update(**{'id': 89, 'size': 2, 'x': 3})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.size, 2)
        self.assertEqual(u1.x, 3)

        u1.update(**{'id': 89, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.size, 2)
        self.assertEqual(u1.x, 3)
        self.assertEqual(u1.y, 4)

    def test_create(self):
        """Test for create function"""

        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

        s1 = Square.create(**{'id': 89, 'size': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)

        s1 = Square.create(**{'id': 89, 'size': 2, 'x': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)

        s1 = Square.create(**{'id': 89, 'size': 2, 
        'x': 3, 'y': 4})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_save_to_file(self):
        """Test for save to file"""
        Base.__Base__nb_objects = 0

        Square.save_to_file(None)
        self.assertEqual(os.path.exists("Square.json"), True)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file(Square(1))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), 
            '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

    def test_save_to_file_empty(self):
        """Test for save to file empty"""
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(f.read(), str)

    def test_load_from_file(self):
        """Test for load from file"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([Square(2)])
        f = Square.load_from_file()
        self.assertEqual(f[0].size, 1)
        self.assertEqual(type(f), Square)
