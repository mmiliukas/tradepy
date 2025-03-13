import os

from alpaca.data.historical.news import NewsClient
from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.trading.client import TradingClient

news_client = NewsClient(
    os.environ.get("ALPACA_API_KEY"),
    os.environ.get("ALPACA_API_SECRET_KEY"),
)

stock_client = StockHistoricalDataClient(
    os.environ.get("ALPACA_API_KEY"),
    os.environ.get("ALPACA_API_SECRET_KEY"),
)

trading_client = TradingClient(
    os.environ.get("ALPACA_API_KEY"),
    os.environ.get("ALPACA_API_SECRET_KEY"),
    paper=True,
)
