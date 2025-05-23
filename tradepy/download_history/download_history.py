import os
import tempfile
from typing import Callable, Optional

import pandas as pd
import yfinance as yf

from tradepy.download import download

HistoryTransform = Optional[Callable[[pd.DataFrame], None]]


def read_history(file_name: str) -> pd.DataFrame:
    return pd.read_csv(file_name, parse_dates=["Date"], index_col="Date")


def download_history(
    symbols: list[str],
    to: str,
    period: str = "max",
    float_format="%.4f",
    transform: HistoryTransform = None,
) -> int:
    with tempfile.TemporaryDirectory(delete=False) as temp_dir:
        # yfinance is using sqlite, and running it inside multiple processes at the same time
        # deadlocks it, so we need to use a different cache location for each process.
        yf.set_tz_cache_location(temp_dir)

        for symbol in symbols:
            history = download(symbol, period=period)

            if history.empty:
                continue

            if transform:
                transform(history)

            file_name = os.path.join(to, f"{symbol}.csv")
            history.to_csv(file_name, float_format=float_format, index=False)

    return len(symbols)
