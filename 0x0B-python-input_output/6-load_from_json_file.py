#!/usr/bin/python3
"""This is the module that will define
a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """This will create a Python
object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
