#!/usr/bin/env python3
"""
Module that provides a function to convert a NumPy ndarray
into a pandas DataFrame with alphabetically labeled columns.
"""
import pandas as pd


def from_numpy(array):
    """
    Create a pandas DataFrame from a NumPy ndarray.

    Parameters:
        array (np.ndarray): The NumPy array used to create the DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with columns labeled alphabetically
        and capitalized (A, B, C, ...). Supports up to 26 columns.
    """
    number_of_columns = array.shape[1]
    name_of_columns = [chr(ord('A') + i) for i in range(number_of_columns)]
    return pd.DataFrame(array, columns=name_of_columns)
