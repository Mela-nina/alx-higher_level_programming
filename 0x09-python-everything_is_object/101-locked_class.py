#!/usr/bin/python3
"""This is  a locked class"""


class LockedClass:
    """
    This only allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
