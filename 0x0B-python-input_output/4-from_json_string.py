#!/usr/bin/python3
"""This is the module that will define
a JSON-to-object function"""


import json


def from_json_string(my_str):
    """This will return the Python object
representation of a JSON string"""
    return json.loads(my_str)
