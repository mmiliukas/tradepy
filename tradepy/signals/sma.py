import pandas as pd


def sma(df: pd.DataFrame, window: int) -> None:
    df["SMA"] = df["Close"].rolling(window=window).mean()
