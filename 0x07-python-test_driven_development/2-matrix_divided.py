#!/usr/bin/python3
"""
Module 2-matrix_divided
This contains function/method that divides all elements of a
matrix by an int/float number and returns new matrix
Requires same size lists of ints or floats, and return in two decimal places
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends in 2 decimal places
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    errorMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(errorMsg)

    newMatrix = []
    elementLen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:  # check if 1-dim is list
            raise TypeError(errorMsg)
        if len(lists) != elementLen:  # check the element size
            raise TypeError("Each row of the matrix must have the same size")
        newList = []
        for i in lists:
            if not isinstance(i, (int, float)):  # is element int/float
                raise TypeError(errorMsg)
            newList.append(round(i/div, 2))  # append to newList
        newMatrix.append(newList)
    return newMatrix
