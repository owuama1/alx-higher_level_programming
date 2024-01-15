#!/usr/bin/python3
"""
This module defines a function for matrix multiplication.

The function matrix_mul takes two matrices as input and returns their product.
It validates the input matrices based on certain requirements.

Requirements:
- Both matrices (m_a and m_b) must be a list of lists of integers or floats.
- Both matrices must not be empty.
- All elements in the matrices must be integers or floats.
- Matrices must be rectangular, i.e., each row should be of the same size.
- The num of cols in m_a must be = the num of rows in m_b for multiplication.

If any of these requirements are not met, the func raises exceptions.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the resulting matrix.

    :param m_a: The first matrix.
    :type m_a: list of lists of integers or floats
    :param m_b: The second matrix.
    :type m_b: list of lists of integers or floats
    :return: The product of the two matrices.
    :rtype: list of lists of integers or floats
    :raises TypeError: If matrices are not properly formatted.
    :raises ValueError: If matrices cannot be multiplied.
    """
    # Validate m_a and m_b
    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not matrix or any(not isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not matrix[0]:
            raise ValueError(f"{name} can't be empty")
        if any(not isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if len(set(len(row) for row in matrix)) > 1:
            raise TypeError(f"Each row of {name} must be of the same size")

    # Validate if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
