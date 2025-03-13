from datetime import date

from alpaca.trading.requests import GetCalendarRequest

from .clients import trading_client


def is_trading_day() -> bool:
    today = date.today()
    calendar = trading_client.get_calendar(GetCalendarRequest(start=today, end=today))
    return len(calendar) > 0
