#!/usr/bin/env python3
"""
This module calculates the marginal probability of obtaining specific data
given various hypothetical probabilities and their corresponding prior beliefs.
"""
import numpy as np
intersection = __import__('1-intersection').intersection


def marginal(x, n, P, Pr):
    """
    Calculates the marginal probability of obtaining data x and n.

    Parameters:
        x (int): Number of patients that develop severe side effects.
        n (int): Total number of patients observed.
        P (numpy.ndarray): 1D array containing hypothetical probabilities.
        Pr (numpy.ndarray): 1D array containing the prior beliefs of P.

    Returns:
        float: The total marginal probability of obtaining the data.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not np.isclose(np.sum(Pr), 1.0):
        raise ValueError("Pr must sum to 1")

    # Calculate intersection probabilities using the imported function
    intersection_probs = intersection(x, n, P, Pr)

    # The marginal probability is the sum of all individual intersection elements
    return np.sum(intersection_probs)
