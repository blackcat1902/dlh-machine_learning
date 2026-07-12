#!/usr/bin/env python3
def flip_switch(df):
    """ Sort in reverse chronological order (descending)."""
    df_sorted = df.sort_index(ascending=False)

    # Transpose the sorted dataframe
    df_transposed = df_sorted.T

    return df_transposed
