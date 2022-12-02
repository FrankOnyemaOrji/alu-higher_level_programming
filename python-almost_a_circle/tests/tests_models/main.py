#!/usr/bin/python3
"""main module"""
from models.square import Square
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 7, 8)
    r2 = Rectangle(2, 4)
    rectangles_input = [r1, r2]

    Rectangle.save_to_file(rectangles_input)

    rectangles_output = Rectangle.load_from_file()

    for r in rectangles_input:
        print("[{}] {}".format(r.id, r))

    print("_ _ _")

    for r in rectangles_output:
        print("[{}] ({}) {}/{} - {}/{}".format(id(r), r))

    print("_ _ _")
    print("_ _ _")

    s1 = Square(10, 7, 8)
    s2 = Square(2, 4)
    squares_input = [s1, s2]

    Square.save_to_file(squares_input)

    squares_output = Square.load_from_file()

    for s in squares_input:
        print("[{}] {}".format(s.id, s))

    print("_ _ _")

    for s in squares_output:
        print("[{}] ({}) {}/{} - {}/{}".format(id(s), s))
