#!/usr/bin/python3
"""This will check if object is an instance
of a class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """This will return true if object is an instance of a
    class or a class that the class in question inherits from
    """
    return (isinstance(obj, a_class))
