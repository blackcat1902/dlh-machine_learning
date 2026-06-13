#!/usr/bin/env python3
"""Contains the Binomial class"""


class Binomial:
    """Represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the binomial distribution

        Args:
            data: A list of data to estimate the distribution
            n: The number of Bernoulli trials
            p: The probability of a "success"
        """
        if data is None:
            # Validation for raw n and p parameters
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            
            self.n = int(n)
            self.p = float(p)
            
        else:
            # Validation for data list
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # 1. Calculate sample mean (x_bar) and sample variance (s^2)
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            # 2. Estimate initial p using Method of Moments
            # variance / mean = 1 - p  ->  p = 1 - (variance / mean)
            # To avoid DivisionByZero if mean is 0
            if mean == 0:
                initial_p = 0.5
            else:
                initial_p = 1.0 - (variance / mean)

            # 3. Estimate n and round it to the nearest integer
            if initial_p <= 0 or initial_p >= 1:
                # Fallback if variance data doesn't fit a valid binomial profile cleanly
                self.n = 1
            else:
                self.n = int(round(mean / initial_p))

            # Guard rails to make sure estimated n is at least 1
            if self.n <= 0:
                self.n = 1

            # 4. Recalculate p based on the strictly rounded integer n
            self.p = float(mean / self.n)
    
    def _factorial(self, num):
        """Helper method to calculate the factorial of a number"""
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of successes

        Args:
            k: The number of successes

        Returns:
            The PMF value for k, or 0 if k is out of range
        """
        # Convert k to an integer as required
        k = int(k)

        # If k is out of range (cannot have fewer than 0 or more than n successes)
        if k < 0 or k > self.n:
            return 0.0

        # Calculate binomial coefficient: n! / (k! * (n - k)!)
        n_fact = self._factorial(self.n)
        k_fact = self._factorial(k)
        nk_fact = self._factorial(self.n - k)
        
        binomial_coefficent = n_fact / (k_fact * nk_fact)

        # Calculate PMF: nCr * (p ** k) * ((1 - p) ** (n - k))
        pmf_value = binomial_coefficent * (self.p ** k) * ((1 - self.p) ** (self.n - k))

        return float(pmf_value)