from datetime import date, datetime

import pandas as pd


def any_to_string(value) -> str:
    if pd.isna(value) or pd.isnull(value):
        return ""

    elif isinstance(value, float):
        return f"{value:,.4f}"

    elif isinstance(value, int):
        return f"{value:,}"

    elif isinstance(value, (datetime, date, pd.Timestamp)):
        return value.strftime("%Y-%m-%d")

    elif value is None:
        return ""

    else:
        return str(value)


def rolling(series: pd.Series, window: int):
    last_n = []
    last = []

    for i in range(len(series) - window):
        chunk = series.iloc[i : i + window].values
        last_n.append(",".join(list(map(any_to_string, chunk))))
        last.append(chunk[-1] if len(chunk) > 0 else None)

    return (
        pd.Series(last_n, index=range(window, len(series))),
        pd.Series(last, index=range(window, len(series))),
    )
