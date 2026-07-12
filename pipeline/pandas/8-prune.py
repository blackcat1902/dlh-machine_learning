#!/usr/bin/env python3
def prune(df):
    # Close sütununda NaN olan satırları kaldır
    df_clean = df.dropna(subset=["Close"])
    return df_clean
