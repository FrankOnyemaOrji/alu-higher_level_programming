#!/usr/bin/python3
"""Defines a base modal class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base instance"""
        Base.__nb_objects += 1
        self.id = id

    @property
    def id(self):
        """Getter for id"""
        return self.__id

    @id.setter
    def id(self, id):
        """Set id"""
        if id is None:
            self.__id = Base.__nb_objects
        else:
            self.__id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string"""
        if list_dictionaries is None or \
                len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_dicts = []
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is not None or len(list_objs) == 0:
                f.write("[]")
            elif type(list_objs) is list:
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 3)
        elif cls.__name__ == "Square":
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                content = f.read()
        except FileNotFoundError:
            return list()

        list_dicts = cls.from_json_string(content)
        list_instances = []
        for dictionary in list_dicts:
            list_instances.append(cls.create(**dictionary))
        return list_instances
