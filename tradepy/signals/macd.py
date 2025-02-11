import pandas as pd


def macd(
    data: pd.DataFrame,
    fast_window: int,
    slow_window: int,
    signal_window: int,
) -> None:
    data["MACD EMA Fast"] = data["Close"].ewm(span=fast_window, adjust=False).mean()
    data["MACD EMA Slow"] = data["Close"].ewm(span=slow_window, adjust=False).mean()
    data["MACD"] = data["MACD EMA Fast"] - data["MACD EMA Slow"]
    data["MACD Signal Line"] = data["MACD"].ewm(span=signal_window, adjust=False).mean()
