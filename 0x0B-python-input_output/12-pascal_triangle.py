#!/usr/bin/python3
"""
Module Name: pascal_triangle
Description: This module provides a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    :param n: The number of rows in Pascal's triangle.
    :return: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
