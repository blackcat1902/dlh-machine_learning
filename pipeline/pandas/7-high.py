#!/usr/bin/env python3
def high(df):
    # Sort by the High column in descending order
    df_sorted = df.sort_values(by="High", ascending=False)
    return df_sorted
