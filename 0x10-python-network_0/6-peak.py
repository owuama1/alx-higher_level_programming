#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak element in a list of unsorted integers.
    A peak element is defined as an element that >=  to its neighbors.
    For corner elements, we need to consider only one neighbor.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element from the list. If the list is empty, returns None.
    """
    if not list_of_integers:
        return None

    return _find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)


def _find_peak_helper(arr, low, high):
    """
    Helper function to find the peak using binary search.

    Args:
        arr (list): The list of integers.
        low (int): The lower index of the current subarray.
        high (int): The higher index of the current subarray.

    Returns:
        int: A peak element from the list.
    """
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    if arr[mid] >= arr[mid + 1]:
        return _find_peak_helper(arr, low, mid)
    return _find_peak_helper(arr, mid + 1, high)
