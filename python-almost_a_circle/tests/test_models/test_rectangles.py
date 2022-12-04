#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """Unittest for Rectangle class"""

    def test_instance(self):
        """Test for instantiation"""
        Base.__Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 12)
        r3 = Rectangle(10, 2, 0, 12)
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(10, -2)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-10, 2)
        
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("10", 2)
        
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(10, "2")
        
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(10, 2, "0")

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(10, 2, 0, "12")

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(10.5, 2)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(10, 2.5)
        
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(10, 2, 0.5)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(10, 2, 0, 12.5)

    def test_area(self):
        """Test for area"""
        a1 = Rectangle(3, 2)
        self.assertEqual(a1.area(), 6)

    def test__str__(self):
        """Test for __str__"""
        s1 = Rectangle(4, 6)
        with patch('sys.stdout', new=StringIO()) as f:
            print(s1)
            self.assertEqual(f.getvalue(), "[Rectangle] (1) 0/0 - 10/2\n")

    def test_display(self):
        """Test for display"""
        d1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            d1.display()
            self.assertEqual(f.getvalue(), "##\n##\n")

        d2 = Rectangle(3, 2, 1)
        with patch('sys.stdout', new=StringIO()) as f:
            d2.display()
            self.assertEqual(f.getvalue(), " ###\n ###\n")
        
        d3 = Rectangle(2, 3, 0, 2)
        with patch('sys.stdout', new=StringIO()) as f:
            d3.display()
            self.assertEqual(f.getvalue(), "\n\n##\n##\n##\n")

    def test_for_dictionary(self):
        """Test for dictionary"""
        d1 = Rectangle(10, 2, 1, 9)
        d1_dictionary = d1.to_dictionary()
        self.assertEqual(d1_dictionary, 
        {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

    def test_update(self):
        """Test for updates"""
        Base.__Base__nb_objects = 0
        u1 = Rectangle(10, 10)
        u1.update()
        self.assertEqual(u1.id, 1)

        u1.update(89)
        self.assertEqual(u1.id, 89)

        u1.update(89, 2)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.id, 89)

        u1.update(89, 2, 3)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.height, 3)
        self.assertEqual(u1.id, 89)

        u1.update(89, 2, 3, 4)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.height, 3)
        self.assertEqual(u1.x, 4)
        self.assertEqual(u1.id, 89)

        u1.update(89, 2, 3, 4, 5)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.height, 3)
        self.assertEqual(u1.x, 4)
        self.assertEqual(u1.y, 5)

        u1.update(**{'id': 89})
        self.assertEqual(u1.id, 89)

        u1.update(**{'id': 89, 'width': 2})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 2)

        u1.update(**{'id': 89, 'width': 2, 'height': 3})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.height, 3)

        u1.update(**{'id': 89, 'width': 2, 'height': 3, 'x': 4})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.height, 3)
        self.assertEqual(u1.x, 4)

        u1.update(**{'id': 89, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(u1.id, 89)
        self.assertEqual(u1.width, 2)
        self.assertEqual(u1.height, 3)
        self.assertEqual(u1.x, 4)
        self.assertEqual(u1.y, 5)

    def test_create(self):
        """Test for create"""

        r1 = Rectangle(**{'id': 89})
        self.assertEqual(r1.id, 89)

        r2 = Rectangle(**{'id': 89, 'width': 2})
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(**{'id': 89, 'width': 2, 'height': 3})
        self.assertEqual(r3.id, 89)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 3)

        r4 = Rectangle(**{'id': 89, 'width': 2,
         'height': 3, 'x': 4})
        self.assertEqual(r4.id, 89)
        self.assertEqual(r4.width, 2)
        self.assertEqual(r4.height, 3)
        self.assertEqual(r4.x, 4)

    def test_save_to_file(self):
        """Test for save to file"""
        Base.__Base__nb_objects = 0

        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
            self.assertEqual(f.read(), str)

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            with open("Rectangle.json", "r") as f:
                self.assertEqual(f.read(),
                '[{"x": 0, "y": 0, "id": 1, '
                ' "height": 2, "width": 1}]')

    def test_save_to_file_empty(self):
        """Test for save to file empty"""
        Base.__Base__nb_objects = 0
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file(self):
        """Test for from file"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        self.assertEqual(Rectangle.from_file(), [])
        Rectangle.save_to_file([Rectangle(1, 2)])
        f = Rectangle.load_from_file()
        self.assertEqual(type(f), list)
        self.assertEqual(f[0].width, 1)
        self.assertEqual(f[0].height, 2)    
