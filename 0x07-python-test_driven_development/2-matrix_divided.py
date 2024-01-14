#!/usr/bin/python3

"""
Module: 0-matrix_divided

This module contains a function matrix_divided that divides all elements
of a matrix by a given divisor.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elems divided by div, rounded to 2 d.p.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
