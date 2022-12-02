#!/usr/bin/python3
"""A rectangle module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a new Square """
        super().__init__(width, height, x, y, id)

    def __str__(self):
        """ Return a string representation of a Square """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,self.width)
    
    @property
    def size(self):
        """ Get/set the size of the square """
        return self.width
    
    @size.setter
    def size(self, value):
        """ Set the size of the square """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the square """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                
    def to_dictionary(self):
        """
        Return square dictionary 
        representation
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
