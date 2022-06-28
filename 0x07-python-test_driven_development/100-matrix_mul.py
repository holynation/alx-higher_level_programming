#!/usr/bin/python3
"""
Module 100-matrix_mul
This contains function/method that does matrix multiplication
Requires same size lists/rows of ints or floats
"""


def matrix_mul(m_a, m_b):
    """
    Returns resulting matrix multiplication
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format
                        ("m_a" if not isinstance(m_a, list) else "m_b"))

    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("{} can't be empty".format
                         ("m_a" if len(m_a) == 0 else "m_b"))

    for eachrow in m_a:
        if type(eachrow) is not list:  # check if m_a is list
            raise TypeError("m_a must be a list of lists")
        for n in eachrow:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(eachrow) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        if len(eachrow) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    for eachrow in m_b:
        if type(eachrow) is not list:  # check if m_b is list
            raise TypeError("m_b must be a list of lists")
        for n in eachrow:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(eachrow) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")

    result = []
    newMatrix = []
    summation = 0
    for rowA in range(len(m_a)):
        result = []
        for colB in range(len(m_b[0])):
            for i in range(len(m_a[0])):
                summation += m_a[rowA][i] * m_b[i][colB]
            result.append(summation)  # append the result
            summation = 0  # reset summation
        newMatrix.append(result)

    return newMatrix
