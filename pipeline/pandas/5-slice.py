#!/usr/bin/env python3
def slice(df):
    selected = df[["High", "Low", "Close", "Volume_(BTC)"]]
    sliced_table = selected.iloc[::60]
    return sliced_table
