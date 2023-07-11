#!/usr/bin/python3
"""This is the module that will define
a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """This will write an object to a
text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
