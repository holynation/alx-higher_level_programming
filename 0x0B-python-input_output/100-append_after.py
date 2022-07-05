#!/usr/bin/python3
"""
Module 100-append_after

Contains function that appends str after lines that include keyword
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)
    I. recreate content in new_text by copying lines over
    II. append new_string after lines if needed
   III. overwrite file from beginning
    """

    with open(filename, mode="r+", encoding="utf-8") as fd:
        new_text = ""
        for line in fd:
            new_text += line
            if search_string in line:
                new_text += new_string
        fd.seek(0)
        fd.write(new_text)
