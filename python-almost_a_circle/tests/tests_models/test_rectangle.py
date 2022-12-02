#!/usr/bin/python
"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from unittest import TestCase


class TestRectanglemethods(unittest.TestCase):
    """Class for testing Rectangle class"""

    def Stater(self):
        """method invoker"""
        Base.__Base__nb_objects = 0

    def test_rectangle_new(self):
        """test for new rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_rectangles_new2(self):
        """test for new rectangle"""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        self.assertEqual(False, r1 == r2)
        self.assertEqual(False, r1.id is r2.id)

    def test_is_Base_instance(self):
        """test if instance of Base"""
        r1 = Rectangle(10, 2)
        self.assertTrue(isinstance(r1, Base), True)

    def test_incorrect_amount_attrs1(self):
        """test for incorrect amount of attributes"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_incorrect_amount_attrs2(self):
        """test for incorrect amount of attributes"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_access_private_attrs(self):
        """test for access to private attributes"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 1)
            print(r1.__width)

    def test_access_private_attrs2(self):
        """test for access to private attributes"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 1)
            print(r1.__height)

    def test_access_private_attrs3(self):
        """test for access to private attributes"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 1)
            print(r1.__x)

    def test_access_private_attrs4(self):
        """test for access to private attributes"""
        with self.assertRaises(AttributeError):
            r1 = Rectangle(1, 1)
            print(r1.__y)

    def test_valide_attrs(self):
        """test to pass a string"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 1)

    def test_valide_attrs2(self):
        """test to pass a string"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "1")

    def test_valide_attrs3(self):
        """test to pass a string"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "1")

    def test_valide_attrs4(self):
        """test to pass a string"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, "1")

    def test_value_attrs(self):
        """test to pass a negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 1)

    def test_value_attrs2(self):
        """test to pass a negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -1)

    def test_value_attrs3(self):
        """test to pass a negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -1)

    def test_value_attrs4(self):
        """test to pass a negative value"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 1, -1)

    def test_new_area1(self):
        """test for area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_new_area2(self):
        """test for area"""
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)
        r1.width = 5
        self.assertEqual(r1.area(), 50)
        r1.height = 3
        self.assertEqual(r1.area(), 15)

    def test_new_area3(self):
        """test for display"""
        r1 = Rectangle(4, 6)
        self.assertEqual(r1.area(), 5)
        r2 = Rectangle(2, 2)
        self.assertEqual(r2.area(), 4)

    def test_new_display1(self):
        """test for display"""
        r1 = Rectangle(4, 6)
        r = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_new_display2(self):
        """test for display"""
        r1 = Rectangle(2, 3)
        r = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r)

        r1.width = 3
        r = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_str(self):
        """test for __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r)

    def test_str2(self):
        """test for __str__"""
        r1 = Rectangle(5, 5, 1)
        r = "[Rectangle] (1) 1/0 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r)

        r1.id = 10
        r1.width = 2
        r1.height = 3
        r = "[Rectangle] (10) 1/0 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r)

    def test_str3(self):
        """test for __str__"""
        r1 = Rectangle(1, 1)
        r = "[Rectangle] (1) 0/0 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r)

        r2 = Rectangle(2, 2)
        r = "[Rectangle] (2) 0/0 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), r)

        r3 = Rectangle(3, 3)
        r = "[Rectangle] (3) 0/0 - 3/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r3)
            self.assertEqual(fake_out.getvalue(), r)

    def test_str4(self):
        """Test for return value"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r1), r)


    def test_display(self):
        """Test for display"""
        r1 = Rectangle(2, 2, 2, 2)
        r = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_display2(self):
        """Test for display"""
        r1 = Rectangle(3, 2, 1, 0)
        r = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r)

        r1.x = 2
        r = "  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_to_dictionary1(self):
        """test for to_dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r = "[Rectangle] (1) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.id, 1)

        r = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(fake_out.getvalue(), r)

    def test_to_dictionary_2(self):
        """test for dictionary returned"""
        r1 = Rectangle(10, 2, 1, 9)
        r = "[Rectangle] (1) 1/9 - 10/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r)

        r2 = Rectangle(1, 1)
        r = "[Rectangle] (2) 0/0 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), r)
        
        r2.update(**r1.to_dictionary())


        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 9)
        self.assertEqual(r1.id, 1)

        r = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(type(r2.to_dictionary()))
            self.assertEqual(fake_out.getvalue(), r)

    def test_dict_to_json(self):
        """test for dictionary to json"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        r = "[{}]".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(json_dictionary)
            self.assertEqual(fake_out.getvalue(), r)

    def test_check_value(self):
        """Test args passed"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def test_check_type(self):
        """Test args passed"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

    def test_create(self):
        """Test for create method"""
        dict = {'id': 89}
        r1 = Rectangle.create(**dict)
        self.assertEqual(r1.id, 89)

    def test_create2(self):
        """Test for create method"""
        dict = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dict)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create3(self):
        """Test for create method"""
        dict = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dict)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create4(self):
        """Test for create method"""
        dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dict)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create5(self):
        """Test for create method"""
        dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dict)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
    
    def test_load_from_file(self):
        """Test for load from json file"""
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file2(self):
        """Test load from json file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        input = [r1, r2]
        Rectangle.save_to_file(input)
        output = Rectangle.load_from_file()

        for i in range(len(input)):
            self.assertEqual(input[i].__str__(), output[i].__str__())
