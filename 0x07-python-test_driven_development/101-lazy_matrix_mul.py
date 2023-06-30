#!/usr/bin/python3.5
"""

This module is composed by a function that multiplies 2 matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ This is the function that multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        The results of the multiplication


    """

    return (np.matmul(m_a, m_b))
