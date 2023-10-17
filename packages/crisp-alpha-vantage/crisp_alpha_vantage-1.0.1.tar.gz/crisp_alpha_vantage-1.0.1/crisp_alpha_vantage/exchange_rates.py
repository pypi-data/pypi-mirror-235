from settings import *


def currency_exchange_rate(from_currency="USD", to_currency="CNY") -> dict:
    """
    ❚ Required: from_currency
    The currency you would like to get the exchange rate for. It can either be a physical currency or digital/crypto currency. For example: from_currency=USD or from_currency=BTC.

    ❚ Required: to_currency
    The destination currency for the exchange rate. It can either be a physical currency or digital/crypto currency. For example: to_currency=USD or to_currency=BTC.

    Examples (click for JSON output)
    US Dollar to Japanese Yen:
    https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo

    Bitcoin to Chinese Yuan:
    https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=demo
    """
    easy_url = URL + f'CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}'
    response = easy_request(easy_url=easy_url)

    return response["Realtime Currency Exchange Rate"]


def history_currency_exchange_rate(from_symbol="USD", to_symbol="CHY"):
    """
    ❚ Required: from_symbol
    A three-letter symbol from the forex currency list. For example: from_symbol=EUR

    ❚ Required: to_symbol
    A three-letter symbol from the forex currency list. For example: to_symbol=USD

    ❚ Optional: outputsize
    By default, outputsize=compact. Strings compact and full are accepted

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey=demo
    https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=full&apikey=demo
    """

    url = URL + f'FX_DAILY&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize=full&apikey={API_KEY}'
    response = requests.get(url).json()
    data_dict = response["Time Series FX (Daily)"]

    data_list = []
    for key, value in data_dict.items():
        value.update({"Date": value})
        data_list.append(value)

    data_df = pd.DataFrame(data_list)
    data_df.rename(columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close"}, inplace=True)
    data_df = data_df[["Date", "Open", "High", "Low", "Close"]].copy()

    return data_df






