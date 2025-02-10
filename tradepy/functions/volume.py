import pandas as pd


def mean_excluding_outliers(series: pd.Series):
    mean = series.mean()
    std_dev = series.std()

    filtered_series = series[
        (series >= mean - 3 * std_dev) & (series <= mean + 3 * std_dev)
    ]

    result = filtered_series.mean()
    return mean if pd.isna(result) else result


def volume_mean(df: pd.DataFrame, window: int = 5) -> None:
    rolling = df["Volume"].rolling(window=window)
    df["Volume Mean"] = rolling.aggregate(mean_excluding_outliers).fillna(0).astype(int)


def volume_weighted(df: pd.DataFrame) -> None:
    typical_price = (df["High"] + df["Low"] + df["Close"]) / 3
    cumulative_price_volume = (typical_price * df["Volume"]).cumsum()
    cumulative_volume = df["Volume"].cumsum()

    df["Volume Weighted"] = cumulative_price_volume / cumulative_volume
