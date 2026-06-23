#!/usr/bin/env python3
"""
This module calculates the intersection of obtaining specific data with
various hypothetical probabilities and their corresponding prior beliefs.
"""
import numpy as np


def intersection(x, n, P, Pr):
    """
    Calculates the intersection of obtaining data x and n with each
    probability in P given prior beliefs Pr.

    Parameters:
        x (int): Number of patients that develop severe side effects.
        n (int): Total number of patients observed.
        P (numpy.ndarray): 1D array containing hypothetical probabilities.
        Pr (numpy.ndarray): 1D array containing the prior beliefs of P.

    Returns:
        numpy.ndarray: 1D array containing the intersection for each
                       probability in P.
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

    # Likelihood calculation (Binomial distribution)
    fact_n = np.math.factorial(n)
    fact_x = np.math.factorial(x)
    fact_nx = np.math.factorial(n - x)
    comb = fact_n / (fact_x * fact_nx)
    likelihood = comb * (P ** x) * ((1 - P) ** (n - x))

    # Intersection: P(Data and Phase) = P(Data | Phase) * P(Phase)
    return likelihood * Pr

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

    # The marginal probability is the sum of all individual intersection elements
    return np.sum(intersection(x, n, P, Pr))
