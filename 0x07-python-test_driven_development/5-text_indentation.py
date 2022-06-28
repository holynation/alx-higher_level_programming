#!/usr/bin/python3
"""
Module 5-text_indentation
This contains function/method that prints text with
2 new lines after each ".", "?", and ":"
Takes in a string as arg
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")  # replace with 2 newline
    listLines = [lines.strip(' ') for lines in text.split('\n')]
    formatLines = "\n".join(listLines)  # appended new line
    print(formatLines, end="")
