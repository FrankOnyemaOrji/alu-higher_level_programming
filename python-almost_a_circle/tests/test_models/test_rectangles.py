#!/usr/bin/python3
"""Unittest for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle(unittest.TestCase):
    """Unittest for Rectangle class"""

    def test_rectangle_is_base(self):
        """Test if Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle(10, 2), Base))

    def test_no_args(self):
        """Test if no arguments passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test if one argument passed"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test if two arguments passed"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test if three arguments passed"""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test if four arguments passed"""
        r1 = Rectangle(2, 2, 2, 2)
        r2 = Rectangle(2, 2, 2, 4)
        self.assertEqual(r1.id, r2.id - 1)
    
    def test_five_args(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_more_than_five_args(self):
        """Test if more than five arguments passed"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
        
    def test_width_is_Private(self):
        """Test if width is an Private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 0).__width)

    def test_height_is_Private(self):
        """Test if height is an Private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 0).__height)
        
    def test_x_is_private(self):
        """Test if x is an private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 0).__x)
        
    def test_y_is_private(self):
        """Test if y is an private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 0).__y)

    def test_width_setter(self):
        """Test if width setter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        r1.width = 20
        self.assertEqual(r1.width, 20)

    def test_width_getter(self):
        """Test if width getter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        self.assertEqual(r1.width, r1.width)

    def test_height_setter(self):
        """Test if height setter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        r1.height = 20
        self.assertEqual(r1.height, 20)

    def test_height_getter(self):
        """Test if height getter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        self.assertEqual(r1.height, r1.height)

    def test_x_setter(self):
        """Test if x setter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        r1.x = 20
        self.assertEqual(r1.x, 20)

    def test_x_getter(self):
        """Test if x getter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        self.assertEqual(10, r1.x)

    def test_y_setter(self):
        """Test if y setter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        r1.y = 20
        self.assertEqual(r1.y, 20)

    def test_y_getter(self):
        """Test if y getter works"""
        r1 = Rectangle(5, 5, 0, 0, 0)
        self.assertEqual(10, r1.y)


class TestRectangle_width(unittest.TestCase):
    """Unittest for Rectangle class width attribute"""

    def test_None_width(self):
        """Test if width is None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """Test if width is a string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)

    def test_float_width(self):
        """Test if width is a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_list_width(self):
        """Test if width is a list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 1)

    def test_tuple_width(self):
        """Test if width is a tuple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 1)

    def test_dict_width(self):
        """Test if width is a dict"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"key": "value"}, 1)

    def test_set_width(self):
        """Test if width is a set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 1)

    def test_complex_width(self):
        """Test if width is a complex"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_bool_width(self):
        """Test if width is a bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_frozenset_width(self):
        """Test if width is a frozenset"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3}), 1)

    def test_range_width(self):
        """Test if width is a range"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(0, 5), 1)

    def test_bytes_width(self):
        """Test if width is a bytes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b"Hello", 1)

    def test_bytearray_width(self):
        """Test if width is a bytearray"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'python'), 2)

    def test_memoryview_width(self):
        """Test if width is a memoryview"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'hello'), 2)

    def test_inf_width(self):
        """Test if width is a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        """Test if width is a float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_zero_width(self):
        """Test if width is 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative_width(self):
        """Test if width is negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 2)
    

class TestRectangle_height(unittest.TestCase):
    """Unittest for Rectangle class height attribute"""

    def test_None_height(self):
        """Test if height is None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        """Test if height is a string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")

    def test_float_height(self):
        """Test if height is a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)
    
    def test_list_height(self):
        """Test if height is a list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])
    
    def test_tuple_height(self):
        """Test if height is a tuple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))
    
    def test_dict_height(self):
        """Test if height is a dict"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"key": "value"})
    
    def test_set_height(self):
        """Test if height is a set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})
    
    def test_complex_height(self):
        """Test if height is a complex"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(5))
    
    def test_bool_height(self):
        """Test if height is a bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_frozenset_height(self):
        """Test if height is a frozenset"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3}))

    def test_range_height(self):
        """Test if height is a range"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(0, 5))
    
    def test_bytes_height(self):
        """Test if height is a bytes"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b"Hello")

    def test_bytearray_height(self):
        """Test if height is a bytearray"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, bytearray(b'python'))

    def test_memoryview_height(self):
        """Test if height is a memoryview"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, memoryview(b'hello'))

    def test_inf_height(self):
        """Test if height is a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'))

    def test_nan_height(self):
        """Test if height is a float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'))
        
    def test_zero_height(self):
        """Test if height is 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
    
    def test_negative_height(self):
        """Test if height is negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -5)

class TestRectangle_x(unittest.TestCase):
    """Unittest for Rectangle class x attribute"""

    def test_None_x(self):
        """Test if x is None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, None)

    def test_str_x(self):
        """Test if x is a string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, "Hello")
    
    def test_float_x(self):
        """Test if x is a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, 5.5)

    def test_list_x(self):
        """Test if x is a list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, [1, 2, 3])

    def test_tuple_x(self):
        """Test if x is a tuple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, (1, 2, 3))

    def test_dict_x(self):
        """Test if x is a dict"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {"key": "value"})
    
    def test_set_x(self):
        """Test if x is a set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {1, 2, 3})

    def test_complex_x(self):
        """Test if x is a complex"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, complex(5))

    def test_bool_x(self):
        """Test if x is a bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, True)

    def test_frozenset_x(self):
        """Test if x is a frozenset"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, frozenset({1, 2, 3}))

    def test_range_x(self):
        """Test if x is a range"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, range(0, 5))

    def test_bytes_x(self):
        """Test if x is a bytes"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, b"Hello")

    def test_bytearray_x(self):
        """Test if x is a bytearray"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, bytearray(b'python'))

    def test_memoryview_x(self):
        """Test if x is a memoryview"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, memoryview(b'hello'))

    def test_inf_x(self):
        """Test if x is a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, float('inf'))

    def test_nan_x(self):
        """Test if x is a float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, float('nan'))


class TestRectangle_y(unittest.TestCase):
    """Unittest for Rectangle class y attribute"""

    def test_None_y(self):
        """Test if y is None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, None)

    def test_str_y(self):
        """Test if y is a string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, "Hello")

    def test_float_y(self):
        """Test if y is a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, 5.5)

    def test_list_y(self):
        """Test if y is a list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, [1, 2, 3])

    def test_tuple_y(self):
        """Test if y is a tuple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (1, 2, 3))
    
    def test_dict_y(self):
        """Test if y is a dict"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {"key": "value"})

    def test_set_y(self):
        """Test if y is a set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {1, 2, 3})

    def test_complex_y(self):
        """Test if y is a complex"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, complex(5))

    def test_bool_y(self):
        """Test if y is a bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, True)

    def test_frozenset_y(self):
        """Test if y is a frozenset"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, frozenset({1, 2, 3}))

    def test_range_y(self):
        """Test if y is a range"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, range(0, 5))

    def test_bytes_y(self):
        """Test if y is a bytes"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, b"Hello")

    def test_bytearray_y(self):
        """Test if y is a bytearray"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, bytearray(b'python'))
    
    def test_memoryview_y(self):
        """Test if y is a memoryview"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, memoryview(b'hello'))

    def test_inf_y(self):
        """Test if y is a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, float('inf'))

    def test_nan_y(self):
        """Test if y is a float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 1, 1, float('nan'))


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittest for Rectangle class order of initialization"""

    def test_width_before_height(self):
        """Test if width is initialized before height"""
        with self.assertRaisesRegex(TypeError, "height 'height' is not defined"):
            Rectangle("invalid width", "invalid height")
        
    def test_hwidth_before_x(self):
        """Test if width is initialized before x"""
        with self.assertRaisesRegex(TypeError, "height 'x' is not defined"):
            Rectangle("invalid width", 1, "invalid x")

    def test_width_before_y(self):
        """Test if width is initialized before y"""
        with self.assertRaisesRegex(TypeError, "height 'y' is not defined"):
            Rectangle("invalid width", 1, 1, "invalid y")

    def test_height_before_x(self):
        """Test if height is initialized before x"""
        with self.assertRaisesRegex(TypeError, "height 'x' is not defined"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        """Test if height is initialized before y"""
        with self.assertRaisesRegex(TypeError, "height 'y' is not defined"):
            Rectangle(1, "invalid height", 1, "invalid y")

    def test_x_before_y(self):
        """Test if x is initialized before y"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "invalid x", "invalid y")

    
class TestRectangle_area(unittest.TestCase):
    """Unittest for Rectangle class area method"""

    def test_area_small(self):
        """Test if area is calculated correctly"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test if area is calculated correctly"""
        r = Rectangle(100, 100)
        self.assertEqual(r.area(), 10000)

    def test_area_changed_attributes(self):
        """Test if area is calculated correctly"""
        r = Rectangle(2, 3)
        r.width = 5
        r.height = 5
        self.assertEqual(r.area(), 25)

    def test_area_args(self):
        """Test if area takes no arguments"""
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.area(1)

        
class TestRectangle_stdout(unittest.TestCase):
    """Unittest for Rectangle class stdout"""

    @staticmethod
    def capture_stdout(r, m):
        """Capture stdout"""
        my_stdout = io.StringIO()
        sys.stdout = my_stdout
        if m == "print":
            print(r)
        else:
            r.display()
        sys.stdout = sys.__stdout__
        return my_stdout
    

    def test_str_method_print_width_height(self):
        """Test if __str__ method prints width and height"""
        r = Rectangle(4, 6)
        my_stdout = TestRectangle_stdout.capture_stdout(r, "print")
        output = "[Rectangle] (1) 0/0 - 4/6"
        self.assertEqual(output, my_stdout.getvalue())

    def test_str_method_print_width_height_x_y(self):
        """Test if __str__ method prints width, height, x and y"""
        r = Rectangle(4, 6, 2, 1)
        output = "[Rectangle] (1) 2/1 - 4/6".format(r.id)
        self.assertEqual(output, str(r))

    def test_str_method_print_width_height_x_y_id(self):
        """Test if __str__ method prints width, height, x, y and id"""
        r = Rectangle(4, 6, 2, 1, 12)
        output = "[Rectangle] ({}) 2/1 - 4/6".format(r.id)
        self.assertEqual(output, str(r))

    def test_str_method_width_height_x_y(self):
        """Test if __str__ method prints width, height, x and y"""
        r = Rectangle(4, 6, 2, 1)
        output = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(output, str(r))

    def test_str_method_changed_attributes(self):
        """Test if __str__ method prints width, height, x and y"""
        r = Rectangle(4, 6, 2, 1)
        r.width = 10
        r.height = 12
        r.x = 3
        r.y = 15
        output = "[Rectangle] ({}) 3/15 - 10/12".format(r.id)
        self.assertEqual(output, str(r))

    def test_display_one_arg(self):
        """Test if display takes one argument"""
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_dispaly_width_height(self):
        """Test if display prints width and height"""
        r = Rectangle(2, 3)
        my_stdout = TestRectangle_stdout.capture_stdout(r, "display")
        output = "##\n##\n##\n"
        self.assertEqual(output, my_stdout.getvalue())

    def test_display_width_height_x(self):
        """Test if display prints width, height and x"""
        r = Rectangle(2, 3, 2)
        my_stdout = TestRectangle_stdout.capture_stdout(r, "display")
        output = "  ##\n  ##\n  ##\n"
        self.assertEqual(output, my_stdout.getvalue())

    def test_display_width_height_y(self):
        """Test if display prints width, height and y"""
        r = Rectangle(2, 3, 0, 2)
        my_stdout = TestRectangle_stdout.capture_stdout(r, "display")
        output = "\n\n##\n##\n##\n"
        self.assertEqual(output, my_stdout.getvalue())

    def test_display_width_height_x_y(self):
        """Test if display prints width, height, x and y"""
        r = Rectangle(2, 3, 2, 2)
        my_stdout = TestRectangle_stdout.capture_stdout(r, "display")
        output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output, my_stdout.getvalue())

    def test_display_one_arg(self):
        """Test if display takes one argument"""
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittest for Rectangle class update method"""

    def test_update_args_zero(self):
        """Test if update takes zero arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        """Test if update takes one argument"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        """Test if update takes two arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        """Test if update takes three arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        """Test if update takes four arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        """Test if update takes five arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))
    
    def test_update_args_None_id(self):
        """Test if update takes None as id"""
        r = Rectangle(10, 10, 10, 10)
        r.update(None)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", format(r.id))

    def test_update_args_None_id_and_more(self):
        """Test if update takes None as id and more arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(None, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", format(r.id))

    def test_update_args_twice(self):
        """Test if update takes two arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_invalid_width_type(self):
        """Test if update takes invalid width type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        """Test if update takes width zero"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        """Test if update takes width negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -1)

    def test_update_args_invalid_height_type(self):
        """Test if update takes invalid height type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """Test if update takes height zero"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, 0)

    def test_update_args_height_negative(self):
        """Test if update takes height negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 2, -1)

    def test_update_args_invalid_x_type(self):
        """Test if update takes invalid x type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        """Test if update takes x negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 2, 3, -1)

    def test_update_args_invalid_y_type(self):
        """Test if update takes invalid y type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        """Test if update takes y negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 2, 3, 4, -1)
    
    def test_update_args_width_before_height(self):
        """Test if update takes width before height"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 3, 4, 5)
        
    def test_update_args_height_before_x(self):
        """Test if update takes height before x"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid", 4, 5)

    def test_update_args_width_before_y(self):
        """Test if update takes width before y"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 3, 4, 5)

    def test_update_args_height_before_y(self):
        """Test if update takes height before y"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid", 4, 5)

    def test_update_args_x_before_y(self):
        """Test if update takes x before y"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid", 5)


class TestRectangle_update_kwargs(unittest.TestCase):
    """unnittest for Rectangle class update method with kwargs"""

    def test_update_kwargs_one(self):
        """Test if update takes one argument"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/1", str(r))

    def test_update_kwargs_two(self):
        """Test if update takes two arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        """Test if update takes three arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3,)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_four(self):
        """Test if update takes four arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))
    
    def test_update_kwargs_five(self):
        """Test if update takes five arguments"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_None_id(self):
        """Test if update takes None id type"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=None)
        output = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(output, str(r))

    def test_update_kwargs_None_id_and_more(self):
        """Test if update takes None id type and more"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=2, height=3)
        output = "[Rectangle] ({}) 10/10 - 2/10".format(r.id)
        self.assertEqual(output, str(r))

    def test_update_kwargs_twice(self):
        """Test if update takes twice"""
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, x=2, height=3)
        r.update(y=3, width=2, height=3)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_invalid_id_type(self):
        """Test if update takes invalid id type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "id must be an integer"):
            r.update(id="invalid")

    def test_update_kwargs_width_zero(self):
        """Test if update takes width zero"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)
    
    def test_update_kwargs_width_negative(self):
        """Test if update takes width negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-1)

    def test_update_kwargs_invalid_height_type(self):
        """Test if update takes invalid height type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """Test if update takes height zero"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        """Test if update takes height negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-1)

    def test_update_kwargs_invalid_x_type(self):
        """Test if update takes invalid x type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """Test if update takes x negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-1)

    def test_update_kwargs_invalid_y_type(self):
        """Test if update takes invalid y type"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """Test if update takes y negative"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-1)

    def test_update_args_and_kwargs(self):
        """Test if update takes args and kwargs"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_key(self):
        """Test if update takes wrong key"""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "unexpected keyword argument"):
            r.update(id=1, width=2, height=3, x=4, y=3, z=4)

def test_update_kwargs_some_wrong_key(self):
        """Test if update takes some wrong key"""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=5, id=1, width=2, x=4, y=3, z=4)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Test class for Rectangle.to_dictionary()"""

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9)
        r_dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r_dictionary, r.to_dictionary())

    def test_to_dirctionary_no_object_change(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertFalse(r1 is r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
