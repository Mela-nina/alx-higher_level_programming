#!/usr/bin/python3
"""This is the module that will define
a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """This will return the JSON representation of a string object"""
    return json.dumps(my_obj)
