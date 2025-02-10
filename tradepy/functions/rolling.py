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
    results = []
    for i in range(len(series) - window):
        chunk = series.iloc[i : i + window].values
        results.append(",".join(list(map(any_to_string, chunk))))
    return pd.Series(results, index=range(window, len(series)))
