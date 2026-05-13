#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    """The Function adds two arrays element-wise."""
    if len(arr1) != len(arr2):
        return None

    result =[]
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result