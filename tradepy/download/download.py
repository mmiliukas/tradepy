from datetime import date

import pandas as pd
import yfinance as yf


def download(
    symbol: str,
    start: str | date | None = None,
    end: str | date | None = None,
    interval="1d",
    period: str = "max",
    progress=False,
) -> pd.DataFrame:
    df = yf.download(
        symbol,
        start=start,
        end=end,
        interval=interval,
        period=period,
        progress=progress,
        group_by="ticker",
        threads=False,
        auto_adjust=True
    )

    if df is None or df.empty:
        return pd.DataFrame()

    result: pd.DataFrame = df[symbol]  # type: ignore
    result = result.reset_index(names=["Date"])

    result["Date"] = result["Date"].dt.date
    result["Symbol"] = symbol

    return result
