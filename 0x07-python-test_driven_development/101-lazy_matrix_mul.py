#!/usr/bin/python3
"""
This module defines a function for matrix multiplication using NumPy.

func lazy_matrix_mul takes 2 matrices as input, represented as lists of lists,
and returns the product using NumPy library. If matrices can't be multiplied,
a ValueError is raised.

Make sure to install NumPy using the command:
pip3 install numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy. Returns result matrix as a formatted str

    :param m_a: The first matrix.
    :type m_a: list of lists of integers or floats
    :param m_b: The second matrix.
    :type m_b: list of lists of integers or floats
    :return: The product of the two matrices as a formatted string.
    :rtype: str
    :raises ValueError: If matrices cannot be multiplied.
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return np.array_str(result)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
