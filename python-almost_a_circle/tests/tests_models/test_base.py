#!/usr/bin/python3
"""Unittest for base.py"""
import os 
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittest for Base class instantiation"""

    def test_no_args(self):
        """Test no args"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Test three bases"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """Test None id"""
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_unique_id(self):
        self.assertEqual(Base(12).id, 12)

    def test_nb_instance_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id -1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_nb_instance_private(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_str_id(self):
        self.assertEqual(Base("Holberton").id, "Holberton")

    def test_float_id(self):
        self.assertEqual(Base(12.5).id, 12.5)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual(Base({"a": 1}).id, {"a": 1})

    def test_bool_id(self):
        self.assertEqual(Base(True).id, True)

    def test_list_id(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_tuple_id(self):
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))

    def test_set_id(self):
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_fronzenset_id(self):
        self.assertEqual(Base(frozenset({1, 2, 3})).id, frozenset({1, 2, 3}))

    def test_range_id(self):
        self.assertEqual(Base(range(5)).id, range(5))

    def test_bytes_id(self):
        self.assertEqual(Base(b"Hello").id, b"Hello")

    def test_bytearray_id(self):
        self.assertEqual(Base(bytearray(5)).id, bytearray(5))

    def test_memoryview_id(self):
        self.assertEqual(Base(memoryview(bytes(5))).id, memoryview(bytes(5)))

    def test_inf_id(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_NaN_id(self):
        self.assertEqual(Base(float('nan')).id, float('nan'))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittest for Base class to_json_string method"""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(type(Base.to_json_string([r.to_dictionary()])), str)

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8) 
        self.assertEqual(len(Base.to_json_string([r.to_dictionary()])), 57)

    def test_to_json_string_rectangle_two_dict(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        self.assertEqual(len(Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])), 114)

    def test_to_json_string_square_type(self):
        s = Square(10, 7, 2)
        self.assertEqual(type(Base.to_json_string([s.to_dictionary()])), str)

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 7, 2)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 49)

    def test_to_json_string_square_two_dict(self):
        s1 = Square(10, 7, 2)
        s2 = Square(2, 4)
        self.assertEqual(len(Base.to_json_string([s1.to_dictionary(), s2.to_dictionary()])), 98)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_None(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

        
class TestBase_save_to_file(unittest.TestCase):
    """Unittest for Base class save_to_file method"""

    @classmethod
    def setUpClass(self):
        """set up for test"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()), 57)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()), 114)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()), 49)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()), 98)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()), 49)

    def test_save_to_file_overwrite(self):
        s = Square(10, 7, 2)
        Square.save_to_file([s])
        s = Square(2, 4)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()), 49)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 2)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittest for Base class from_json_string method"""

    def test_from_json_string_type(self):
        input = [{"id": 89, "width": 10, "height": 4,}]
        json_input = Rectangle.to_json_string(input)
        ouput = Rectangle.from_json_string(json_input)
        self.assertEqual(type(ouput), list)

    def test_from_json_string_one_rectangle(self):
        input = [{"id": 89, "width": 10, "height": 4, "x": 7,}]
        json_input = Rectangle.to_json_string(input)
        ouput = Rectangle.from_json_string(json_input)
        self.assertEqual(input, ouput)

    def test_from_json_string_two_rectangles(self):
        input = [{"id": 89, "width": 10, "height": 4, "x": 7,}, {"id": 7, "width": 1, "height": 7, "x": 9,}]
        json_input = Rectangle.to_json_string(input)
        ouput = Rectangle.from_json_string(json_input)
        self.assertEqual(input, ouput)

    def test_from_json_string_one_square(self):
        input = [{"id": 89, "size": 10, "x": 7,}]
        json_input = Square.to_json_string(input)
        ouput = Square.from_json_string(json_input)
        self.assertEqual(input, ouput)

    def test_from_json_string_two_squares(self):
        input = [{"id": 89, "size": 10, "x": 7,}, {"id": 7, "size": 1, "x": 9,}]
        json_input = Square.to_json_string(input)
        ouput = Square.from_json_string(json_input)
        self.assertEqual(input, ouput)

    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittest for Base class create method"""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 1, 12)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (12) 1/1 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 1, 12)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (12) 1/1 - 3/5", str(r2))

    def test_create_rectangle_id(self):
        r1 = Rectangle(3, 5, 1, 1, 12)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_square_rectangle_equal(self):
        r1 = Rectangle(3, 5, 1, 1, 12)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 1, 1, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (12) 1/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 1, 1, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (12) 1/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 1, 1, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_square_equal(self):
        s1 = Square(3, 1, 1, 12)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittest for load from file method of base class"""

    @classmethod
    def tearDown(cls):
        """Tear down method"""
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 1, 1, 2)
        Rectangle.save_to_file([r1, r2])
        rectangle_list_output = Rectangle.load_from_file()
        self.assertTrue(all(type(b) == Rectangle for b in rectangle_list_output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 1, 1)
        s2 = Square(2, 1, 1, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 1, 1)
        s2 = Square(2, 1, 1, 2)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))
    
    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 1, 1)
        s2 = Square(2, 1, 1, 2)
        Square.save_to_file([s1, s2])
        square_list_output = Square.load_from_file()
        self.assertTrue(all(type(b) == Square for b in square_list_output))

    def test_load_from_file_empty(self):
        output = Rectangle.load_from_file()
        self.assertEqual(output, [])

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], 1)

    
if __name__ == '__main__':
    unittest.main()
