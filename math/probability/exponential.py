#!/usr/bin/env python3
"""Contains the Exponential class"""


class Exponential:
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.0):
        """Initializes the exponential distribution"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # lambtha = 1 / mean of data
            self.lambtha = float(1 / (sum(data) / len(data)))

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period

        Args:
            x: The time period

        Returns:
            The PDF value for x, or 0 if x is out of range
        """
        if x < 0:
            return 0

        # e is approximately 2.7182818285
        e = 2.7182818285
        
        return self.lambtha * (e ** (-self.lambtha * x))
    