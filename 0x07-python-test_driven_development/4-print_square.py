#!/usr/bin/python3
"""
Module 4-print_square
This contains function/method that prints square with #'s
Takes an int size as arg
"""


def print_square(size):
    """
    Prints square with #'s with int size as arg
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
