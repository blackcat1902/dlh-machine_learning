#!/usr/bin/env python3

def index(df):
    """
    Set the Timestamp column as the index of the DataFrame.

    Returns:
        pd.DataFrame: The modified DataFrame with Timestamp as index.
    """
    df = df.set_index("Timestamp")
    return df
