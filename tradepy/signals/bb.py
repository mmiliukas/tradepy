import pandas as pd


def bb(data: pd.DataFrame, window: int, std_dev: float) -> None:
    data["BB Middle Band"] = data["Close"].rolling(window=window).mean()
    data["BB Std Dev"] = data["Close"].rolling(window=window).std()
    data["BB Upper Band"] = data["BB Middle Band"] + (std_dev * data["BB Std Dev"])
    data["BB Lower Band"] = data["BB Middle Band"] - (std_dev * data["BB Std Dev"])
    data["BB"] = data["Close"] < data["Lower Band"]
