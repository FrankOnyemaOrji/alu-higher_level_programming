#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines"""


def text_indentation(text):
    """prints text with two lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in ".?:":
        text = (i + "\n\n").join([j.strip(" ") for j in text.split(i)])
    print("{}".format(text), end="")
