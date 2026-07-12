#!/usr/bin/env python3
import pandas as pd


def rename(df):
    """
    Rename the Timestamp column to Datetime, convert it to datetime,
    and return only Datetime and Close columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing a 'Timestamp' column.

    Returns:
        pd.DataFrame: Modified DataFrame with 'Datetime' and 'Close' columns.
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df = df[["Datetime", "Close"]]
    return df
