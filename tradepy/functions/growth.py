import pandas as pd


def growth(df: pd.DataFrame) -> None:
    df["Growth High"] = (df["High"] / df["Open"]) - 1
    df["Growth Low"] = (df["Low"] / df["Open"]) - 1
