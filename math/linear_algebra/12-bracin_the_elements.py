#!/usr/bin/env python3
"""Performs element-wise operations"""

import numpy as np


def np_elementwise(mat1, mat2):
    """Returns element-wise add, sub, mul, and div"""
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2

    return (add, sub, mul, div)
