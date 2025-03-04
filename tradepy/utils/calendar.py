from datetime import date, timedelta
import pandas_market_calendars as pmc


def get_previous_trading_date() -> date:
    cal = pmc.get_calendar("NYSE")

    yesterday = date.today() - timedelta(days=1)
    ten_days_ago = yesterday - timedelta(days=10)

    valid_days = cal.valid_days(start_date=ten_days_ago, end_date=yesterday)
    return valid_days[-1].date()
