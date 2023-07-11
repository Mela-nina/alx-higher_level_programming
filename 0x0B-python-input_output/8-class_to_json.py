#!/usr/bin/python3
"""This is the module that will define
a Python class-to-JSON function"""


def class_to_json(obj):
    """This will return the dictionary representation of
a simple data structure"""
    return obj.__dict__
