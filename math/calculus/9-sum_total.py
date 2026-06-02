#!/usr/bin/env python3

def summation_i_squared(n):
    """ a function that calculates"""
    if not isinstance(n, int) or isinstance(n, bool) or n<0:
        return None
    return n*(n+1)*(2*n+1)//6

n=9
result = summation_i_squared(9)
print(result)
