#!/usr/bin/env python3
"""
Defines the MultiNormal class representing a
Multivariate Normal distribution
"""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """
        Initializes the MultiNormal class.

        Parameters:
        - data: numpy.ndarray of shape (d, n) containing the data set
        """
        # Check if data is a 2D numpy.ndarray
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        # Check if data contains multiple data points
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Calculate the mean along axis 1
        # Result shape will be (d, 1)
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Center the data by subtracting the mean
        data_centered = data - self.mean

        # Calculate the covariance matrix
        # Since data is (d, n), data_centered.T is (n, d)
        # resulting in (d, d)
        self.cov = np.matmul(data_centered, data_centered.T) / (n - 1)
        