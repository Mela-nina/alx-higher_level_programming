#!/usr/bin/python3
"""This will check if object is an instance of a class"""


def is_same_class(obj, a_class):
    """This will return true if object is an instance
    of the class, otherwise return false
    """
    return (type(obj) == a_class)
