#!/usr/bin/env python3
""" the calculation sum of the squared numbers """

def summation_i_squared(n):
    """ a function that calculates
    
    Args:
        n: The stopping condition.

    Returns:
        Integer sum of squares.
    
    """

    if not isinstance(n, int)  or  n<0:
        return None
    
    return n*(n+1)*(2*n+1)//6
