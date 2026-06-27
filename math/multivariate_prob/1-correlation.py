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
    # Check if C is a numpy.ndarray
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    # Check if C is a 2D square matrix
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    # Extract the variances from the diagonal
    variance = np.diag(C)

    # Calculate standard deviations by taking the square root of variances
    std_dev = np.sqrt(variance)

    # Compute the correlation matrix: C_ij / (std_dev_i * std_dev_j)
    corr = C / np.outer(std_dev, std_dev)

    return corr
