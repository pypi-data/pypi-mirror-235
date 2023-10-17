from settings import *


# def daily_stock_df(symbol: str, start_date="2000-01-01", end_date="2099-12-31"):
#     """
#         ❚ Required: function
#         The time series of your choice. In this case, function=TIME_SERIES_INTRADAY
#
#         ❚ Required: symbol
#         The name of the equity of your choice. For example: symbol=IBM
#
#         ❚ Required: interval
#         Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
#
#         ❚ Optional: adjusted
#         By default, adjusted=true and the output time series is adjusted by historical split and dividend events. Set adjusted=false to query raw (as-traded) intraday values.
#
#         ❚ Optional: extended_hours
#         By default, extended_hours=true and the output time series will include both the regular trading hours and the extended trading hours (4:00am to 8:00pm Eastern Time for the US market). Set extended_hours=false to query regular trading hours (9:30am to 4:00pm US Eastern Time) only.
#
#         ❚ Optional: month
#         By default, this parameter is not set and the API will return intraday data for the most recent days of trading. You can use the month parameter (in YYYY-MM format) to query a specific month in history. For example, month=2009-01. Any month in the last 20+ years since 2000-01 (January 2000) is supported.
#
#         ❚ Optional: outputsize
#         By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the intraday time series; full returns trailing 30 days of the most recent intraday data if the month parameter (see above) is not specified, or the full intraday data for a specific month in history if the month parameter is specified. The "compact" option is recommended if you would like to reduce the data size of each API call.
#
#         ❚ Optional: datatype
#         By default, datatype=json. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.
#
#         Examples (click for JSON output)
#         The API will return the most recent 100 intraday OHLCV bars by default when the outputsize parameter is not set
#         https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
#
#         Query the most recent full 30 days of intraday data by setting outputsize=full
#         https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo
#
#         Query intraday data for a given month in history (e.g., 2009-01). Any month in the last 20+ years (since 2000-01) is supported
#         https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&month=2009-01&outputsize=full&apikey=demo
#
#         Downloadable CSV file:
#         https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo&datatype=csv
#
#         Tip: the intraday data (including 20+ years of historical data) is updated at the end of each trading day for all users by default.
#     """
#     url = URL + f'TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}'
#     response = requests.get(url).json()
#
#     data_list = []
#     for key, value in response["Time Series (Daily)"].items():
#         value.update({"Date": key})
#         data_list.append(value)
#
#     stock_df = pd.DataFrame(data_list)
#     stock_df.rename(
#         columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"},
#         inplace=True)
#     stock_df = stock_df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
#
#     needed_df = stock_df[(stock_df.Date >= start_date) & (stock_df.Date <= end_date)].copy()
#     needed_df = needed_df.astype({"Open": "float", "High": "float", "Low": "float", "Close": "float", "Volume": "int"})
#     needed_df.sort_values(by=["Date"], ascending=True, inplace=True)
#
#     return needed_df.round(2)
#
#
# def weekly_stock_df(symbol: str, start_date="2000-01-01", end_date="2099-12-31"):
#     """
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=AAPL&apikey={API_KEY}'
#
#     ❚ Required: function
#     The time series of your choice. In this case, function=TIME_SERIES_WEEKLY_ADJUSTED
#
#     ❚ Required: symbol
#     The name of the equity of your choice. For example: symbol=IBM
#
#     ❚ Optional: datatype
#     By default, datatype=json. Strings json and csv are accepted with the following specifications:
#     json returns the weekly time series in JSON format; csv returns the time series as a
#     CSV (comma separated value) file.
#     """
#     url = URL + f'TIME_SERIES_WEEKLY&symbol={symbol}&outputsize=full&apikey={API_KEY}'
#     response = requests.get(url).json()
#
#     data_list = []
#     for key, value in response["Weekly Time Series"].items():
#         value.update({"Date": key})
#         data_list.append(value)
#
#     stock_df = pd.DataFrame(data_list)
#     stock_df.rename(
#         columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"},
#         inplace=True)
#     stock_df = stock_df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
#
#     needed_df = stock_df[(stock_df.Date >= start_date) & (stock_df.Date <= end_date)].copy()
#     needed_df = needed_df.astype({"Open": "float", "High": "float", "Low": "float", "Close": "float", "Volume": "int"})
#     needed_df.sort_values(by=["Date"], ascending=True, inplace=True)
#
#     return needed_df.round(2)
#
#
# def monthly_stock_df(symbol: str, start_date="2000-01-01", end_date="2099-12-31"):
#     """
#     url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo'
#
#     ❚ Required: function
#     The time series of your choice. In this case, function=TIME_SERIES_MONTHLY
#
#     ❚ Required: symbol
#     The name of the equity of your choice. For example: symbol=IBM
#     """
#     url = URL + f'TIME_SERIES_MONTHLY&symbol={symbol}&outputsize=full&apikey={API_KEY}'
#     response = requests.get(url).json()
#
#     data_list = []
#     for key, value in response["Monthly Time Series"].items():
#         value.update({"Date": key})
#         data_list.append(value)
#
#     stock_df = pd.DataFrame(data_list)
#     stock_df.rename(
#         columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"},
#         inplace=True)
#     stock_df = stock_df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()
#
#     needed_df = stock_df[(stock_df.Date >= start_date) & (stock_df.Date <= end_date)].copy()
#     needed_df = needed_df.astype({"Open": "float", "High": "float", "Low": "float", "Close": "float"})
#     # OverflowError: Python int too large to convert to C long: 所以 Volume 这一列并没有转成 int 类型
#     needed_df.sort_values(by=["Date"], ascending=True, inplace=True)
#
#     return needed_df.round(2)


def get_stock_df(symbol: str, freq="Daily", start_date="2000-01-01", end_date="2099-12-31") -> pd.DataFrame:
    freq_dict = {"daily": {"function": "TIME_SERIES_DAILY", "series": "Time Series (Daily)"},
                 "weekly": {"function": "TIME_SERIES_WEEKLY", "series": "Weekly Time Series"},
                 "monthly": {"function": "TIME_SERIES_MONTHLY", "series": "Monthly Time Series"}}
    real_freq = freq_dict[freq]
    url = URL + f'{real_freq["function"]}&symbol={symbol}&outputsize=full&apikey={API_KEY}'
    response = requests.get(url).json()

    data_list = []
    for key, value in response[real_freq["series"]].items():
        value.update({"Date": key})
        data_list.append(value)

    stock_df = pd.DataFrame(data_list)
    stock_df.rename(
        columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"},
        inplace=True)
    stock_df = stock_df[["Date", "Open", "High", "Low", "Close", "Volume"]].copy()

    needed_df = stock_df[(stock_df.Date >= start_date) & (stock_df.Date <= end_date)].copy()
    needed_df = needed_df.astype({"Open": "float", "High": "float", "Low": "float", "Close": "float"})
    # OverflowError: Python int too large to convert to C long: 所以 Volume 这一列并没有转成 int 类型
    needed_df.sort_values(by=["Date"], ascending=True, inplace=True)

    return needed_df.round(2)


def quote_endpoint(symbol="AAPL") -> dict:
    """
    returns the latest price and volume information for a ticker of your choice.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo

    https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=300135.SHZ&apikey=demo

    Downloadable CSV file:
    https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo&datatype=csv
    """
    easy_url = URL + f"GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response["Global Quote"]


def symbol_search_endpoint(keywords="AAPL") -> list:
    """
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'

    The Search Endpoint returns the best-matching symbols and market information based on
    keywords of your choice. The search results also contain match scores that provide you
    with the full flexibility to develop your own search and filtering logic.

    ❚ Required: keywords
    A text string of your choice. For example: keywords=microsoft.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo
    https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tencent&apikey=demo
    https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BA&apikey=demo
    https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=SAIC&apikey=demo

    Downloadable CSV file:
    https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=BA&apikey=demo&datatype=csv
    """
    easy_url = URL + f"function=SYMBOL_SEARCH&keywords={keywords}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response['bestMatches']


def global_market_status() -> list:
    """
    url = 'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey=demo'

    returns the current market status (open vs. closed) of major trading venues
    for equities, forex, and cryptocurrencies around the world.
    """
    easy_url = URL + f"MARKET_STATUS&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response['markets']
