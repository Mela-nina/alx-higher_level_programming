#!/usr/bin/python3
"""This module will define a class MyInt that inherits from int"""


class MyInt(int):
    """This inverts int operators == and !="""

    def __eq__(self, value):
        """This will override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """This will override != operator with == behavior"""
        return self.real == value
