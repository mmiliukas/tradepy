import numpy as np
import pandas as pd


def tsl(df: pd.DataFrame, start_index: int, tslatr=-6, ttpatr=3) -> None:
    df["PC"] = df["Close"].shift(1)
    df["High-Low"] = df["High"] - df["Low"]
    df["High-PC"] = abs(df["High"] - df["PC"])
    df["Low-PC"] = abs(df["Low"] - df["PC"])
    df["TR"] = df[["High-Low", "High-PC", "Low-PC"]].max(axis=1)
    df["ATR"] = df["TR"].rolling(window=14, min_periods=14).mean()

    df["RollingATRStop"] = np.nan
    df["RollingTakeProfit"] = np.nan
    stop, tp = None, None

    for i in df.index:
        if i < start_index:
            continue
        atr = df.at[i, "ATR"]
        if pd.isna(atr):
            continue
        close = df.at[i, "Close"]
        high = df.at[i, "High"]
        new_stop = close + tslatr * atr
        new_tp = close + ttpatr * atr  # high
        stop = max(stop, new_stop) if stop is not None else new_stop
        tp = max(tp, new_tp) if tp is not None else new_tp
        df.at[i, "RollingATRStop"] = stop
        df.at[i, "RollingTakeProfit"] = tp
