from .settings import *


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
