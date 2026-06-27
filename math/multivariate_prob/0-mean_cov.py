#!/usr/bin/env python3
"""Calculates the mean and covariance of a data set"""
import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.

    Parameters:
    - X: numpy.ndarray of shape (n, d) containing the data set

    Returns:
    - mean: numpy.ndarray of shape (1, d) containing the mean of the data set
    - cov: numpy.ndarray of shape (d, d) containing the covariance matrix
    """
    # Check if X is a 2D numpy.ndarray
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    # Check if X contains multiple data points
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean along the columns, keeping dimensions as (1, d)
    mean = np.mean(X, axis=0, keepdims=True)

    # Center the data by subtracting the mean
    X_centered = X - mean

    # Calculate the covariance matrix: (X_centered^T @ X_centered) / (n - 1)
    cov = np.matmul(X_centered.T, X_centered) / (n - 1)

    return mean, cov


X_test = np.array([[12, 30, 10], [36, -30, 15], [-30, 100, -20], [15, -20, 25]])
result = mean_cov(X_test)
print(result)