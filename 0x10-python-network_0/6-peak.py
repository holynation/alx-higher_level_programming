#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    temp_list_integers = list_of_integers
    start = 0
    end = len(l)-1

    if temp_list_integers[start] > temp_list_integers[start+1]:
        return temp_list_integers[start]
    if temp_list_integers[end] > temp_list_integers[end-1]:
        return temp_list_integers[end]

    mid = (start+end)//2
    if temp_list_integers[mid-1] < temp_list_integers[mid] and
    temp_list_integers[mid+1] < temp_list_integers[mid]:
        return temp_list_integers[mid]
    if temp_list_integers[mid] < temp_list_integers[mid-1]:
        return find_peak(temp_list_integers[start:mid+1])
    elif temp_list_integers[mid] < temp_list_integers[mid+1]:
        return find_peak(temp_list_integers[mid:end+1])
    else:
        return temp_list_integers[start]
