#!/usr/bin/python3
"""
Module 3-say_my_name
This contains method that prints out "My name is <first name> <last name>"
Takes in two args as strings: first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("{:s} must be a string".
                        format("first_name" if isinstance(last_name, str)
                               else "last_name"))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
