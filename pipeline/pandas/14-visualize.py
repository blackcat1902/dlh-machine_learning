#!/usr/bin/env python3
import pandas as pd


def visualize(df):

    
    """
    Transform and aggregate cryptocurrency OHLCV data for visualization.

    Steps:
    - Remove Weighted_Price column.
    - Rename Timestamp to Date.
    - Convert UNIX timestamps to datetime.
    - Index on Date.
    - Fill missing Close with previous row's value.
    - Fill missing High, Low, Open with same row's Close.
    - Fill missing Volume_(BTC) and Volume_(Currency) with 0.
    - Select data from 2017 onward.
    - Resample daily and aggregate:
        High: max
        Low: min
        Open: mean
        Close: mean
        Volume_(BTC): sum
        Volume_(Currency): sum

    Returns:
        pd.DataFrame: Transformed DataFrame before plotting.
    """
    # Remove Weighted_Price
    df = df.drop(columns=["Weighted_Price"], errors="ignore")

    # Rename Timestamp → Date
    df = df.rename(columns={"Timestamp": "Date"})

    # Convert UNIX timestamp → datetime
    df["Date"] = pd.to_datetime(df["Date"], unit="s")

    # Index on Date
    df = df.set_index("Date")

    # Fill Close with previous row
    df["Close"] = df["Close"].fillna(method="ffill")

    # Fill High, Low, Open with same row's Close
    for col in ["High", "Low", "Open"]:
        df[col] = df[col].fillna(df["Close"])

    # Fill volumes with 0
    df[["Volume_(BTC)", "Volume_(Currency)"]] = (
        df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(0)
    )

    # Filter 2017 and beyond
    df = df.loc["2017":]

    # Daily resampling and aggregation
    daily = df.resample("D").agg({
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum"
    })

    return daily
