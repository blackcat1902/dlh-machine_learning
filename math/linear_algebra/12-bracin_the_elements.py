#!/usr/bin/env python3
import numpy as np

def np_elementwise(mat1, mat2):
    """Performs element-wise operations on two arrays.
    Returns: tuple (addition, subtraction, multiplication, division)
    """
    return (mat1 + mat2,
            mat1 - mat2,
            mat1 * mat2,
            mat1 / mat2)
