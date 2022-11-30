#!/usr/bin/python3
"""Defines a function that prints a text with 2 new lines"""


def text_indentation(text):
    """prints text with two lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    q = 0
    while q < len(text) and text[q] == ' ':
        q += 1

    while q < len(text):
        print(text[q], end="")
        if text[q] == '.' or text[q] == '?' or text[q] == ':':
            if text[q] in ".?:":
                print("\n")
            q += 1
            while q < len(text) and text[q] == ' ':
                q += 1
            continue
        q += 1
