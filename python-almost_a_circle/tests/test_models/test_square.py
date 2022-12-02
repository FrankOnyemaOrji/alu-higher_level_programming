#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.base import Base
from models.square import Square
import io
import sys


class TestSquare_instantiation(unittest.TestCase):
    """Unit tests for Square class instantiation"""

    def test_is_base(self):
        """Test if Square is subclass of Base"""
        self.assertTrue(issubclass(Square(10), Base))

    def test_is_rectangle(self):
        """Test if Square is subclass of Rectangle"""
        self.assertTrue(issubclass(Square(10), Square))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.iid, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2,)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id)

    def test_four_args(self):
        self.assertEqual(Square(10, 2, 2, 12).id, 12)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 2, 12).__size)

    def test_size_getter(self):
        self.assertEqual(Square(10, 2, 2, 12).size, 10)

    def test_size_setter(self):
        s1 = Square(10, 2, 2, 12)
        s1.size = 20
        self.assertEqual(s1.size, 20)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(Square(10, 2, 2, 12).x, 2)

    def test_y_getter(self):
        self.assertEqual(Square(10, 2, 2, 12).y, 2)


class TestSquare_size(unittest.TestCase):
    """Unit tests for Square class size"""

    def test_None_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square("Hello")
    
    def test_float_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(1.5)

    def test_list_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square([1, 2, 3])

    def test_tuple_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square((1, 2, 3))

    def test_dict_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square({"a": 1, "b": 2})

    def test_set_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square({1, 2})

    def test_frozenset_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(frozenset({1, 2}))


    def test_bool_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(True)

    def test_complex_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(complex(1))
    
    def test_zero_size(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(0, 2)

    def test_negative_size(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-1, 2)

    def test_range_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(range(1, 10))

    def test_bytes_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(b"Hello")

    def test_bytearray_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(bytearray(10))

    def test_memoryview_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(memoryview(bytes(5)))

    def test_inf_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(float('inf'))
        
    def test_nan_size(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(float('nan'))

    
class TestSquare_x(unittest.TestCase):
    """Unittest for Square class x"""

    def test_None_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, "Hello")

    def test_float_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, 1.5)

    def test_list_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, [1, 2, 3])
        
    def test_tuple_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, (1, 2, 3))

    def test_dict_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, {"a": 1, "b": 2})
        
    def test_set_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, {1, 2})

    def test_frozenset_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, frozenset({1, 2}))
        
    def test_bool_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, True)
        
    def test_complex_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, complex(1))
        
    def test_range_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, range(1, 10))
    
    def test_bytes_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, b"Hello")
    
    def test_bytearray_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, bytearray(10))

    def test_memoryview_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, memoryview(bytes(5)))

    def test_inf_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, float('inf'))
    
    def test_nan_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, float('nan'))

    def test_negative_x(self):
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Square(1, -1)


class TestSquare_y(unittest.TestCase):
    """Unittest for Square class y"""

    def test_None_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, "Hello")
    
    def test_float_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, 1.5)

    def test_complex_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, complex(1))

    def test_dict_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, {1, 2})

    def test_tuple_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, frozenset({1, 2}))
    
    def test_range_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, range(1, 10))

    def test_bytes_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, b"Hello")

    def test_bytearray_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, bytearray(10))
        
    def test_memoryview_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, memoryview(bytes(5)))

    def test_inf_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, float('inf'))

    def test_nan_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, float('nan'))

    def test_negative_y(self):
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Square(1, 2, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittest for Square class order of initialization"""

    def test_size_before_x(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square("Invalid", "Invalid x")

    def test_size_before_y(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square("Invalid", 1, "Invalid y")

    def test_x_before_y(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, "Invalid x", "Invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittest for Square class area"""

    def test_area_small(self):
        self.assertEqual(Square(10, 0, 0, 1).area(), 100)

    def test_area_large(self):
        s = Square(100, 0, 0, 1)
        self.assertEqual(s.area(), 10000)

    def test_area_changed_attributes(self):
        s = Square(10, 0, 0, 1)
        s.size = 100
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unit test for Square class stdout"""

    def test_stdout_small(s, m):
        """capture stdout"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        if m == "print":
            print(s)
        else:
            s.display()
        sys.stdout = sys.__stdout__
        return capturedOutput

    
    def test_str_method_print_size(self):
        s = Square(1, 0, 0, 1)
        capturedOutput = self.test_stdout_small(s, "print")
        correctOutput = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(capturedOutput, correctOutput.getvalue())

    def test_str_method_print_x(self):
        s = Square(3)
        capturedOutput = self.test_stdout_small(s, "print")
        correctOutput = "[Square] ({}) 0/0 - 3\n".format(s.id)
        self.assertEqual(capturedOutput, correctOutput.getvalue())

    def test_str_method_size_x(self):
        s = Square(3, 4)
        correctOutput = "[Square] ({}) 4/0 - 3\n".format(s.id)
        self.assertEqual(str(s), correctOutput)

    def test_str_method_size_x_y(self):
        s = Square(3, 4, 5)
        correctOutput = "[Square] ({}) 4/5 - 3\n".format(s.id)
        self.assertEqual(str(s), correctOutput)

    def test_str_method_size_x_y_id(self):
        s = Square(3, 4, 5, 6)
        correctOutput = "[Square] (6) 4/5 - 3\n"
        self.assertEqual(str(s), correctOutput)

    def test_str_method_changed_attributes(self):
        s = Square(3, 4, 5, 6)
        s.size = 10
        s.x = 20
        s.y = 30
        s.id = 40
        correctOutput = "[Square] (40) 20/30 - 10\n"
        self.assertEqual(str(s), correctOutput)

    def test_display_size(self):
        s = Square(1, 0, 0, 1)
        capturedOutput = TestSquare_stdout.capture_stdout(s, "display")
        correctOutput = "##\n##\n"
        self.assertEqual(capturedOutput, correctOutput)

    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    def test_display_size_x(self):
        s = Square(3, 2, 0, 1)
        capturedOutput = TestSquare_stdout.capture_stdout(s, "display")
        correctOutput = "  ###\n  ###\n  ###\n"
        self.assertEqual(capturedOutput, correctOutput)

    def test_display_size_y(self):
        s = Square(3, 0, 2, 1)
        capturedOutput = TestSquare_stdout.capture_stdout(s, "display")
        correctOutput = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(capturedOutput, correctOutput)

    def test_display_size_x_y(self):
        s = Square(3, 2, 2, 1)
        capturedOutput = TestSquare_stdout.capture_stdout(s, "display")
        correctOutput = "\n\n  ###\n  ###\n  ###\n"
        self.assertEqual(capturedOutput, correctOutput)

    def test_display_one_arg(self):
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittest for Square class update args"""

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(s.size, 2)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual(s.size, 2)

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correctoutput = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correctoutput, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (89) 2/4 - 3", str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (89) 2/4 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, msg="width must be an integer"):
            s.update(89, "2")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, msg="width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, msg="width must be > 0"):
            s.update(89, -1)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, msg="x must be an integer"):
            s.update(89, 2, "3")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be an integer"):
            s.update(98, 1, 2, "2")

    def test_update_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "3")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "2", "3")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "2", 3, "4")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 2, "3", "4")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittest for Square class update kwargs"""

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2)
        self.assertEqual(s.size, 2)

    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3)
        self.assertEqual(s.size, 2)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correctoutput = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correctoutput, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3, y=4)
        s.update(id=4, size=3, x=2, y=89)
        self.assertEqual("[Square] (89) 2/89 - 3", str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3, y=4)
        s.update(id=4, size=3, x=2, y=89)
        self.assertEqual("[Square] (89) 2/89 - 3", str(s))
    
    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="2")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-1)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="3")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-2)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="3")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-4)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=3)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=2, x=3, y=4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittest for Square class to_dictionary method"""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 9)
        correctoutput = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertEqual(correctoutput, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 9)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertFalse(s1 is s2)

    def test_to_dictionary_args(self):
        s = Square(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

if __name__ == '__main__':
    unittest.main()
