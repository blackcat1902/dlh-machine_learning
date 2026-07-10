#!/usr/bin/env python3

def array(df):
    # Select last 10 rows of High and Close
    selected = df[['High', 'Close']].tail(10)

    # Convert to numpy array
    arr = selected.to_numpy()

    return arr
