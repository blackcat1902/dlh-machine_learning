#!/usr/bin/env python3
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Concatenate two OHLCV DataFrames (bitstamp and coinbase).

    - Indexes both dataframes on their Timestamp columns.
    - Selects rows from df2 up to and including timestamp 1417411920.
    - Concatenates selected df2 rows on top of df1.
    - Adds keys: 'bitstamp' for df2 and 'coinbase' for df1.

    Returns:
        pd.DataFrame: The concatenated DataFrame.
    """
    # Index both dataframes
    df1 = index(df1)
    df2 = index(df2)

    # Select df2 rows up to timestamp 1417411920
    df2_selected = df2.loc[:1417411920]

    # Concatenate with keys
    result = pd.concat(
        [df2_selected, df1],
        keys=["bitstamp", "coinbase"] )
    
    return result
