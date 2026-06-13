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

            # Calculate the sample variance (divide by N - 1 for Bessel's correction)
            variance = sum((d - self.mean) ** 2 for d in data) / (len(data) - 1)

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
    
    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value

        Args:
            x: The x-value

        Returns:
            The PDF value for x
        """
        # Approximations for pi and e
        pi = 3.1415926536
        e = 2.7182818285

        # Breakdown the PDF formula components
        coefficient = 1 / (self.stddev * ((2 * pi) ** 0.5))
        exponent = -0.5 * (((x - self.mean) / self.stddev) ** 2)

        return coefficient * (e ** exponent)
    
    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value

        Args:
            x: The x-value

        Returns:
            The CDF value for x
        """
        # Calculate the internal value for the error function
        erf_input = (x - self.mean) / (self.stddev * (2 ** 0.5))

        # Absolute value to handle symmetry
        val = abs(erf_input)

        # Approximation constants for erf(x)
        a1 = 0.0705230784
        a2 = 0.0422820123
        a3 = 0.0092705272
        a4 = 0.0001520143
        a5 = 0.0002765672
        a6 = 0.0000430638

        # Compute the polynomial inside the denominator
        poly = (1 + a1*val + a2*(val**2) + a3*(val**3) +
                a4*(val**4) + a5*(val**5) + a6*(val**6))

        # This gives the erf for the ABSOLUTE value
        erf_approx = 1 - (1 / (poly ** 16))
        
        # Restore the negative sign if the original erf_input was negative
        if erf_input < 0:
            erf_approx = -erf_approx

        # Calculate final CDF using the standard formula: 0.5 * (1 + erf(z / sqrt(2)))
        final_cdf = 0.5 * (1 + erf_approx)
        
        return final_cdf
