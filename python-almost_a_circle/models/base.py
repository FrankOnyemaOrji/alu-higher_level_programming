#!/usr/bin/python3
"""Defines a base modal class"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                r = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(r))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""
        r = str(cls.__name__) + ".json"
        try:
            with open(r, "r") as f:
                e = (cls.create(**d) for d in Base.from_json_string(f.read()))
                return [e]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize a CSV file to a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fieldnames)
                return [cls.create(**obj) for obj in reader]
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares"""
        t = turtle.Turtle()
        t.shape("turtle")
        t.pensize(3)
        t.screen.bgcolor('#b7312c')
        t.color('#ffffff')

        for rect in list_rectangles:
            t.showturtle()
            t.penup()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color('#b5e3d8')
        for square in list_squares:
            t.showturtle()
            t.penup()
            t.goto(square.x, square.y)
            t.down()
            for i in range(4):
                t.forward(square.size)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
