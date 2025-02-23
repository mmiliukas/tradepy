import pandas as pd

from .bb import bb
from .macd import macd


def test_bb():
    df = pd.DataFrame({"Close": [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]})

    bb(df, window=3, std_dev=2)

    assert df["BB Middle Band"][2] == 102
    assert df["BB Middle Band"][3] == 104

    assert df["BB Std Dev"][2] == 2.0
    assert df["BB Std Dev"][3] == 2.0

    assert df["BB Upper Band"][2] == 106.0
    assert df["BB Lower Band"][2] == 98.0


def test_macd():
    df = pd.DataFrame({"Close": [100, 102, 104, 106, 108, 110, 112, 114, 116, 118]})
    macd(df, fast_window=3, slow_window=5, signal_window=2)

    assert round(df["MACD EMA Fast"][2], 1) == 102.5
    assert round(df["MACD EMA Slow"][2], 1) == 101.8

    assert round(df["MACD"][2], 1) == 0.7

    assert round(df["MACD Signal Line"][2], 1) == 0.6
    assert round(df["MACD"][5], 1) == 1.5
    assert round(df["MACD Signal Line"][5], 1) == 1.4
