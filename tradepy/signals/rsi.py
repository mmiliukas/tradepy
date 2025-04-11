import pandas as pd


def rsi(df: pd.DataFrame, period: int) -> None:
    series = df["Close"]
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rsi = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rsi))
