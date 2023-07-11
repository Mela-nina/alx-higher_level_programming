#!/usr/bin/python3
"""

Module is composed by a function prints a message

"""


def say_my_name(first_name, last_name=""):
    """ This is the unction that prints "My name is <first name> <last name>"

    Args:
        first_name: The first name
        last_name: The last name

    Returns:
        no return

    Raises:
        TypeError: if first_name or last_name is not a string


    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
