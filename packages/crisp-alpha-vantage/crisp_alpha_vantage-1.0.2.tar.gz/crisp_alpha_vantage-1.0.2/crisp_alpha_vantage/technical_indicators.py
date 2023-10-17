from .settings import *


def technical_indicators(symbol="AAPL", function="SMA", interval="weekly", time_period=10, series_type="close"):
    """"
    Technical indicator APIs for a given equity or currency exchange pair, derived from the underlying time series
    based stock API and forex data. All indicators are calculated from adjusted time series data to eliminate
    artificial price/volume perturbations from historical split and dividend events.

    ❚ Required: function
    The technical indicator of your choice. In this case, function=SMA
    accept=[EMA, WMA, DEMA, TEMA, TRIMA, KAMA, MAMA, T3, RSI, WILLR, ADX, ADXR, ]
    premium accept = [VWAP, MACD]

    ❚ Required: symbol
    The name of the ticker of your choice. For example: symbol=IBM

    ❚ Required: interval
    Time interval between two consecutive data points in the time series. The following values are supported:
    1min, 5min, 15min, 30min, 60min, daily, weekly, monthly

    ❚ Optional: month
    Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
    for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
    By default, this parameter is not set and the technical indicator values will be calculated based on
    the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute intraday
    technical indicators for a specific month in history. For example, month=2009-01.
    Any month equal to or later than 2000-01 (January 2000) is supported.

    ❚ Required:time_period
    Number of data points used to calculate each moving average value.
    Positive integers are accepted (e.g., time_period=60, time_period=200)

    ❚ Required: series_type
    The desired price type in the time series. Four types are supported: close, open, high, low

    Examples (click for JSON output)
    Equity:
    https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey=demo

    Forex (FX) or cryptocurrency pair:
    https://www.alphavantage.co/query?function=SMA&symbol=USDEUR&interval=weekly&time_period=10&series_type=open&apikey=demo
    """
    pass


def ti_no_period(symbol="AAPL", function="SMA", interval="weekly", series_type="close"):
    """
    :param symbol:
    :param function: [MACDEXT, STOCH, STOCHF, STOCHRSI]
    :param interval:
    :param series_type:
    :return:
    """
    pass
