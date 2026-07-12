#!/usr/bin/env python3
def prune(df):
    """
    Removes rows where the 'Close' column has NaN values.

    Parameters:
        df (pd.DataFrame): Input dataframe.

    Returns:
        pd.DataFrame: Dataframe with NaN values in 'Close' removed.
    """
    return df.dropna(subset=["Close"])
