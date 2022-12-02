#!/usr/bin/python3
"""Module for Sqaure class"""
import unittest
from io import StringIO
from unittest.mock import patch
from unittest import TestCase
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """Class for testing for square class"""

    def starter(self):
        """Methods invoker"""
        Base.___Base__nb_objects = 0

    def test_square(self):
        """Test new square"""
        s1 = Square(5)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 0)
        self.assertEqual(s1.height, 0)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_square_2(self):
        """Test new square with attrs"""
        s1 = Square(5, 2, 3, 4)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def test_new_square(self):
        """Test new squares"""
        s1 = Square(5, 1)
        s2 = Square(2, 2)
        self.assertEqual(False, s1 == s2)
        self.assertEqual(False, s1.id is s2.id)

    def test_is_Base_instance(self):
        """Test if is instance of Base"""
        s1 = Square(5)
        self.assertEqual(True, isinstance(s1, Base))

    def test_is_Rectangle_instance(self):
        """Test if is instance of Rectangle"""
        s1 = Square(5)
        self.assertEqual(True, isinstance(s1, Rectangle))

    def test_incorrect_amount_attrs(self):
        """Test incorrect amount of attrs"""
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_incorrect_amount_attrs_2(self):
        """Test incorrect amount of attrs"""
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)

    def test_access_private_attrs(self):
        """Test access to private attrs"""
        with self.assertRaises(AttributeError):
            s1 = Square(1)
            s1.__width

    def test_access_private_attrs_2(self):
        """Test access to private attrs"""
        with self.assertRaises(AttributeError):
            s1 = Square(1)
            s1.__height

    def test_access_private_attrs_3(self):
        """Test access to private attrs"""
        with self.assertRaises(AttributeError):
            s1 = Square(1)
            s1.__x

    def test_access_private_attrs_4(self):
        """Test access to private attrs"""
        with self.assertRaises(AttributeError):
            s1 = Square(1)
            s1.__y

    def test_valide_attrs(self):
        """Test valide attrs"""
        with self.assertRaises(TypeError):
            s1 = Square("1", 2, 2)

    def test_valide_attrs_2(self):
        """Test valide attrs"""
        with self.assertRaises(TypeError):
            s1 = Square(1, "2", 2)

    def test_valide_attrs_3(self):
        """Test valide attrs"""
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, "2")

    def test_value_attrs(self):
        """Test value attrs"""
        with self.assertRaises(ValueError):
            s1 = Square(0)

    def test_value_attrs_2(self):
        """Test value attrs"""
        with self.assertRaises(ValueError):
            s1 = Square(1, -2)

    def test_value_attrs_3(self):
        """Test value attrs"""
        with self.assertRaises(ValueError):
            s1 = Square(1, 2, -2)

    def test_area(self):
        """Test area method"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_area_2(self):
        """Test area method"""
        s1 = Square(5, 2, 3)
        self.assertEqual(s1.area(), 25)
        s1.size = 10
        self.assertEqual(s1.area(), 100)

    def test_load_from_file(self):
        """load from json file"""
        load = Square.load_from_file()
        self.assertEqual(load, load)

    def test_display(self):
        """Test string representation"""
        s1 = Square(4)
        r = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_display_2(self):
        """Test string representation"""
        s1 = Square(2, 2)
        r = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)

        s1.size = 5
        r = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_str(self):
        """Test string return value"""
        s1 = Square(4, 2, 1, 12)
        r = "[Square] (12) 2/1 - 4"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

    def test_str2(self):
        """Test __str__ return value"""
        s1 = Square(5, 1)
        r = "[Square] (1) 1/0 - 5"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)
        
        s1.id = 1
        s1.size = 11
        r = "[Square] (1) 1/0 - 11"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

    def test_str3(self):
        """Test string return value"""
        s1 = Square(5)
        r = "[Square] (1) 0/0 - 5"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)
        
        s2 = Square(2, 2, 2)
        r = "[Square] (2) 2/2 - 2"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), r)

        s3 = Square(10, 10, 10, 10)
        r = "[Square] (10) 10/10 - 10"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s3)
            self.assertEqual(fake_out.getvalue(), r)

    def test_str_4(self):
        """Test __str__ return value"""
        s1 = Square(5, 1, 2, 3)
        r = "[Square] (3) 1/2 - 5"
        self.assertEqual(s1.__str__(), r)

    def test_update(self):
        """Test string method"""
        s1 = Square(10, 10, 10)
        r = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_update_2(self):
        """Test method"""
        s1 = Square(3)
        r = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)

        s1.x = 1
        r = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)
        
        s1.y = 2
        r = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), r)

    def test_update_3(self):
        """Test update method"""
        s1 = Square(3)
        r = "[Square] (1) 0/0 - 3"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        s1.update(10)
        r = "[Square] (10) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)
    
    def test_update_4(self):
        """Test update method"""
        s1 = Square(3)
        r = "[Square] (1) 0/0 - 3"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        s1.update(10)
        r = "[Square] (10) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

    def test_updatw_5(self):
        """Test update method"""
        s1 = Square(3)
        r = "[Square] (1) 0/0 - 3"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        s1.update(10, 2, 2, 2)
        r = "[Square] (10) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        s1.update(y=2)
        r = "[Square] (10) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        s1.update(id=1, size=10)
        r = "[Square] (1) 2/2 - 10\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

    def test_update_6(self):
        """Test update method"""
        s1 = Square(3)
        r = "[Square] (1) 0/0 - 3"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)
        
        dict = {'size': 3, 'y': 5}
        s1.update(**dict)
        r = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(),r)

    def test_update_7(self):
        """Test update method"""
        s1 = Square(7)
        r = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)
        
        dict = {'id': 10, 'x': '5', 'y': '5'}
        with self.assertRaises(TypeError):
            s1.update(**dict)

    def test_to_dict(self):
        """Test dictionary method"""
        s1 = Square(10, 2, 1)
        r = "[Square] (1) 2/1 - 10"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 6)

        r = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(type(s1.to_dictionary()))
            self.assertEqual(fake_out.getvalue(), r)

    def test_dict_2(self):
        """Test dictionary method"""
        s1 = Square(10, 2, 1)
        r = "[Square] (1) 2/1 - 10"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), r)

        s2 = Square(1, 1)
        r = "[Square] (2) 1/0 - 1"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(s2)
            self.assertEqual(fake_out.getvalue(), r)

        s1_dict = s1.to_dictionary()
        s2.update(**s1_dict)

        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        r = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(type(s2.to_dictionary()))
            self.assertEqual(fake_out.getvalue(), r)

    def test_dict_to_json(self):
        """Test Dictionary to JSON string"""
        s1 = Square(2)
        s1_dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([s1_dictionary])
        r = "[{}]\n".format(s1_dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(json_dictionary)
            self.assertEqual(fake_out.getvalue(), r.replace("'", '\"'))

    def test_json_file(self):
        """test json file"""
        s1 = Square(2)
        dict = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dict])
        r = "[{}]\n".format(dict.__str__())
        r = r.replace("'", '\"')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(json_dictionary)
            self.assertEqual(fake_out.getvalue(), r)

        Square.save_to_file([s1])
        r = "[Square] (1) 0/0 - 2\n"
        r = r.replace("'", '\"')

        with open("Square.json", "r") as f:
            r2 = f.read()

            self.assertEqual(r2, r)        

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create(self):
        """ Test create method """
        dict = {'id': 89}
        s1 = Square.create(**dict)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dict = {'id': 89, 'size': 1}
        s1 = Rectangle.create(**dict)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """
        dict = {'id': 89, 'size': 1, 'x': 2}
        s1 = Rectangle.create(**dict)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dict = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dict)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        input = [s1, s2]
        Square.save_to_file(input)
        output = Square.load_from_file()

        for i in range(len(input)):
            self.assertEqual(input[i].__str__(), output[i].__str__())
