#!/usr/bin/python3


#test_base.py
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

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
    
    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)
    
    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_public(self):
        b1 = Base(12)
        b1.id = 15
        self.assertEqual(b1.id, 15)
    
    def test_id_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
        
    def test_str_type(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_type(self):
        self.assertEqual(5.5, Base(5.5).id)
    
    def test_complex_type(self):
        self.assertEqual(5 + 5j, Base(5 + 5j).id)
    
    def test_list_type(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)
    
    def test_dict_type(self):
        self.assertEqual({"hello": 5}, Base({"hello": 5}).id)
    
    def test_tuple_type(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)
    
    def test_set_type(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_type(self):
        self.assertEqual(frozenset([1, 2, 3]), Base(frozenset([1, 2, 3])).id)
    
    def test_range_type(self):
        self.assertEqual(range(5), Base(range(5)).id)
    
    def test_bytes_type(self):
        self.assertEqual(b"python", Base(b"python").id)

    def test_bytearray_type(self):
        self.assertEqual(bytearray(5), Base(bytearray(5)).id)
    
    def test_memoryview_type(self):
        self.assertEqual(memoryview(bytes(5)), Base(memoryview(bytes(5))).id)

    def test_inf_type(self):
        self.assertEqual(float("inf"), Base(float("inf")).id)
    
    def test_nan_type(self):
        self.assertEqual(float("nan"), Base(float("nan")).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)
        
class TestBase_to_json_string(unittest.TestCase):
    """Test cases for Base.to_json_string()"""

    def test_to_json_string_rectangle_type(self):
        p = Rectangle(10, 7, 2, 8,6)
        self.assertTrue(type(Base.to_json_string([p.to_dictionary()])) is str)
    
    def test_to_json_string_rectangle_one_dict(self):
        p = Rectangle(10, 7, 2, 8,6)
        self.assertEqual(Base.to_json_string([p.to_dictionary()]), '[{"x": 2, "width": 10, "id": 6, "height": 7, "y": 8}]')
    
    def test_to_json_string_rectangle_two_dicts(self):
        p1 = Rectangle(10, 7, 2, 8,6)
        p2 = Rectangle(2, 4, 0, 0, 1)
        self.assertEqual(Base.to_json_string([p1.to_dictionary(), p2.to_dictionary()]), '[{"x": 2, "width": 10, "id": 6, "height": 7, "y": 8}, {"x": 0, "width": 2, "id": 1, "height": 4, "y": 0}]')
    
    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(type(Base.to_json_string([s.to_dictionary()])) is str)

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])) == 39)
        
    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        self.assertEqual(len(Base.to_json_string([s1.to_dictionary(), s2.to_dictionary()])) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")
    
    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([1])


class Test_save_to_file(unittest.TestCase):
    """Unittests for save_to_file() method"""

    @classmethod
    def teraDown(self):
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except IOError:
            pass
    
    def test_save_to_file_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()) == 53)
    
    def save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        r2 = Rectangle(2, 4, 0, 0, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()) == 106)

    def test_save_to_file_square(self):
        s = Square(10, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()) == 39)
    
    def test_save_to_file_two_squares(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()) == 78)

    def test_save_to_file_cls_name_for_file(self):
        s = Square(10, 2, 3, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
       s = Square(9, 2, 39, 2)
       Square.save_to_file([s])
       s = Square(10, 7, 2, 8)
       Square.save_to_file([s])
       with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()) == 39)

    def test_save_to_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), "[]")
    
    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()
    
    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), "[]")

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class Test_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string() method"""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (6) 2/8 - 10/7", str(r2))
    
    def test_create_rectangle_is(self):
        r1 = Rectangle(5, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
    
    def test_create_rectangle_equal(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
    
    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))
    
    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))
    
    def test_create_square_equal(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1, s2)


class Test_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file() method"""

    @classmethod
    def setUpClass(self):
        """setup class"""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        r2 = Rectangle(2, 4, 0, 0, 1)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_output[0]))
    
    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        list_ouput = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_ouput[1]))
    
    def test_load_from_file_rectangle_type(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_ouput = Rectangle.load_from_file()
        self.assertTrue(all(type(x) is Rectangle for x in list_ouput))
    
    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        list_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        list_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_output[1]))
    
    def test_load_from_file_square_type(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        list_output = Square.load_from_file()
        self.assertTrue(all(type(x) is Square for x in list_output))
    
    def test_load_from_file_no_file(self):
        list_output = Square.load_from_file()
        self.assertEqual(list_output, [])

if __name__ == "__main__":
    unittest.main()
