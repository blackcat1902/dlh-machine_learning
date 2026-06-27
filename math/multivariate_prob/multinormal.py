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

    def pdf(self, x):
        """
        Calculates the PDF at a specific data point.

        Parameters:
        - x: numpy.ndarray of shape (d, 1) containing the data point

        Returns:
        - The value of the PDF (float)
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.cov.shape[0]

        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # Calculate determinant and inverse of the covariance matrix
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        # Calculate the normalization factor: 1 / sqrt((2 * pi)^d * det)
        norm_factor = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)

        # Calculate the exponent term: -0.5 * (x - mu).T @ inv @ (x - mu)
        x_centered = x - self.mean
        exponent = -0.5 * np.matmul(np.matmul(x_centered.T, inv), x_centered)

        # Extract the scalar value from the 1x1 matrix result of the exponent
        pdf_value = norm_factor * np.exp(exponent[0][0])
        return pdf_value

    def pdf(self, x):
        """
        Calculates the PDF at a specific data point.

        Parameters:
        - x: numpy.ndarray of shape (d, 1) containing the data point

        Returns:
        - The value of the PDF (float)
        """
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.cov.shape[0]

        if len(x.shape) != 2 or x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # Calculate determinant and inverse of the covariance matrix
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)

        # Calculate the normalization factor: 1 / sqrt((2 * pi)^d * det)
        norm_factor = 1.0 / np.sqrt(((2 * np.pi) ** d) * det)

        # Calculate the exponent term: -0.5 * (x - mu).T @ inv @ (x - mu)
        x_centered = x - self.mean
        exponent = -0.5 * np.matmul(np.matmul(x_centered.T, inv), x_centered)

        # Extract the scalar value from the 1x1 matrix result of the exponent
        pdf_value = norm_factor * np.exp(exponent[0][0])

        return pdf_value
    