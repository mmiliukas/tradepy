import pandas as pd


def download_symbols(
    source: str = "https://raw.githubusercontent.com/mmiliukas/screeners/main/tickers.csv",
    exclude_exchange: list[str] = ["PNK"],
    include_screeners: list[str] = ["Winners 10"],
):
    df = pd.read_csv(source)

    if "Exchange" in df.columns:
        if exclude_exchange and len(exclude_exchange):
            df = df[~df["Exchange"].isin(exclude_exchange)]

    if "Screener Max" in df.columns:
        if include_screeners and len(include_screeners):
            df = df[df["Screener Max"].isin(include_screeners)]

    return list(zip(df["Symbol"].to_list(), df["Screener Max"].to_list()))
