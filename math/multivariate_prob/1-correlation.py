#!/usr/bin/env python3
"""Calculates a correlation matrix from a covariance matrix"""
import numpy as np


def correlation(C):
    """
    Calculates the correlation matrix.

    Parameters:
    - C: numpy.ndarray of shape (d, d) containing a covariance matrix

    Returns:
    - numpy.ndarray of shape (d, d) containing the correlation matrix
    """
    
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

   
    variance = np.diag(C)

   
    std_dev = np.sqrt(variance)


    corr = C / np.outer(std_dev, std_dev)

    return corr
