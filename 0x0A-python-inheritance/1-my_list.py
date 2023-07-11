#!/usr/bin/python3
"""This module will inherit from the list class"""


class MyList(list):
    """This is a class that inherits from list"""
    def print_sorted(self):
        """This prints a sorted list"""
        print(sorted(self))
