#!/usr/bin/env python3
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Rearrange MultiIndex so Timestamp is first level and concatenate
    bitstamp and coinbase data between timestamps 1417411980 and 1417417980.

    - Indexes both dataframes on their Timestamp columns.
    - Selects rows from df2 and df1 within the timestamp range.
    - Concatenates df2 (bitstamp) above df1 (coinbase).
    - Ensures Timestamp becomes the first level of the MultiIndex.
    - Ensures chronological order.

    Returns:
        pd.DataFrame: The concatenated DataFrame.
    """
    # Index both dataframes
    df1 = index(df1)
    df2 = index(df2)

    # Select timestamp range
    start = 1417411980
    end = 1417417980

    df1_sel = df1.loc[start:end]
    df2_sel = df2.loc[start:end]

    # Concatenate with keys
    result = pd.concat(
        [df2_sel, df1_sel],
        keys=["bitstamp", "coinbase"]
    )

    # Swap MultiIndex levels so Timestamp becomes level 0
    result = result.swaplevel(0, 1)

    # Sort by Timestamp (now first level)
    result = result.sort_index()

    return result
