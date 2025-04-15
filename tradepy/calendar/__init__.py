from datetime import datetime

import pandas_market_calendars as mcal
import pytz


class NyseCalendar:
    def __init__(self):
        self.__nyse = mcal.get_calendar("NYSE")
        self.__eastern = pytz.timezone("US/Eastern")

        now = datetime.now(self.__eastern)
        today = now.date()

        schedule = self.__nyse.schedule(start_date=today, end_date=today)
        if schedule.empty:
            raise Exception("The market is closed today")

        row = schedule.iloc[0]

        self.__market_open = row["market_open"].astimezone(self.__eastern)
        self.__market_close = row["market_close"].astimezone(self.__eastern)

    def hours_passed(self):
        result = self.time()
        if result is None:
            return -1
        return result[0]

    def hours_remaining(self):
        result = self.time()
        if result is None:
            return -1
        return result[1]

    def time(self):
        now = datetime.now(self.__eastern)

        if self.__market_open <= now <= self.__market_close:
            time_since_open = now - self.__market_open
            time_until_close = self.__market_close - now
            return time_since_open.seconds / 3600, time_until_close.seconds / 3600

        return None
