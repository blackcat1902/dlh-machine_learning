#!/usr/bin/env python3


def analyze(df):
    """
    Compute descriptive statistics for all columns except Timestamp.

    Returns:
        pd.DataFrame: A new DataFrame containing the statistics.
    """
    # Remove Timestamp if it exists
    if "Timestamp" in df.columns:
        data = df.drop(columns=["Timestamp"])
    else:
        data = df

    # Compute descriptive statistics
    stats = data.describe()

    return stats
