#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON string-to-object conversion function."""
import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string."""
    return json.loads(my_str)
