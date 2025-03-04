import pandas as pd


def growth(df: pd.DataFrame) -> None:
    df["Growth High"] = (df["High"] / df["Open"]) - 1
    df["Growth Low"] = (df["Low"] / df["Open"]) - 1
    df["Growth High 1"] = (df["High"].shift(-1) / df["Open"]) - 1
    df["Growth High 2"] = (df["High"].shift(-2) / df["Open"]) - 1
    df["Growth Low 1"] = (df["Low"].shift(-1) / df["Open"]) - 1
    df["Growth Low 2"] = (df["Low"].shift(-2) / df["Open"]) - 1
