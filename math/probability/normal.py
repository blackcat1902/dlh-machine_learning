#!/usr/bin/env python3
"""Contains the Normal class"""


class Normal:
    """Represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the normal distribution

        Args:
            data: A list of data to estimate the distribution
            mean: The mean of the distribution
            stddev: The standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate the mean
            self.mean = float(sum(data) / len(data))

            # Calculate the variance (sum of squared differences from the mean)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)

            # Calculate the standard deviation (square root of variance)
            self.stddev = float(variance ** 0.5)
            
    def z_score(self, x):
        """Calculates the z-score of a given x-value

        Args:
            x: The x-value

        Returns:
            The z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score

        Args:
            z: The z-score

        Returns:
            The x-value of z
        """
        return (z * self.stddev) + self.mean
    