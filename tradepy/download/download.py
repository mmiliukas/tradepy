from datetime import date

import pandas as pd
import yfinance as yf


def download(
    ticker: str,
    start: str | date | None = None,
    end: str | date | None = None,
    interval="1d",
    period: str = "max",
    progress=False,
) -> pd.DataFrame:
    history = yf.download(
        ticker,
        start=start,
        end=end,
        interval=interval,
        period=period,
        progress=progress,
        group_by="ticker",
        threads=False,
    )
    return history[ticker]
