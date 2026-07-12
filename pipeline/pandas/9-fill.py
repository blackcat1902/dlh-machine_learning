#!/usr/bin/env python3
import pandas as pd

def fill(df):
    """
    Clean and fill a cryptocurrency OHLCV DataFrame.

    - Removes the Weighted_Price column (ignores if missing).
    - Fills missing Close values with the previous row's Close.
    - Fills missing High, Low, and Open values with the row's Close.
    - Sets missing Volume_(BTC) and Volume_(Currency) to 0.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Remove Weighted_Price safely
    df = df.drop(columns=["Weighted_Price"], errors="ignore")

    # Fill Close using previous row
    df["Close"] = df["Close"].fillna(method="ffill")

    # Fill High, Low, Open using Close of same row
    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])

    # Fill both volume columns at once
    df[["Volume_(BTC)", "Volume_(Currency)"]] = (
        df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(0)
    )

    return df
