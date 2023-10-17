from .settings import *


def company_overview(symbol="AAPL") -> dict:
    """
    returns the company information, financial ratios, and other key metrics for the equity
    specified. Data is generally refreshed on the same day a company reports its latest earnings and financials.

    Example (click for JSON output)
    https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
    """
    easy_url = URL + f"OVERVIEW&symbol={symbol}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response


def income_statement(symbol="AAPL") -> dict:
    """
    returns the annual and quarterly income statements for the company of interest,
    with normalized fields mapped to GAAP and IFRS taxonomies of the SEC.
    Data is generally refreshed on the same day a company reports its latest earnings and financials.

    Example - annual & quarterly income statements for IBM (click for JSON output)
    https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
    """
    easy_url = URL + f"INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response


def balance_sheet(symbol="AAPL") -> dict:
    """
    returns the annual and quarterly balance sheets for the company of interest,
    with normalized fields mapped to GAAP and IFRS taxonomies of the SEC.
    Data is generally refreshed on the same day a company reports its latest earnings and financials.

    Example - annual & quarterly balance sheets for IBM (click for JSON output)
    https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey=demo
    """
    easy_url = URL + f"BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response


def cash_flow(symbol="AAPL") -> dict:
    """
    returns the annual and quarterly cash flow for the company of interest,
    with normalized fields mapped to GAAP and IFRS taxonomies of the SEC.
    Data is generally refreshed on the same day a company reports its latest earnings and financials.

    Example - annual & quarterly cash flows for IBM (click for JSON output)
    https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=demo
    """
    easy_url = URL + f"CASH_FLOW&symbol={symbol}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response


def earnings(symbol="AAPL") -> dict:
    """
    returns the annual and quarterly earnings (EPS) for the company of interest.
    Quarterly data also includes analyst estimates and surprise metrics.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=demo
    """
    easy_url = URL + f"EARNINGS&symbol={symbol}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response


def earnings_calendar(horizon="3month") -> pd.DataFrame:
    """
    returns a list of company earnings expected in the next 3, 6, or 12 months.

    ❚ Optional: symbol
    By default, no symbol will be set for this API. When no symbol is set,
    the API endpoint will return the full list of company earnings scheduled.
    If a symbol is set, the API endpoint will return the expected earnings
    for that specific symbol. For example, symbol=IBM

    ❚ Optional: horizon
    By default, horizon=3month and the API will return a list of expected company earnings
    in the next 3 months. You may set horizon=6month or horizon=12month to query
    the earnings scheduled for the next 6 months or 12 months, respectively.

    Examples
    To ensure optimal API response time, this endpoint uses the CSV format which is more memory-efficient than JSON.

    Querying all the company earnings expected in the next 3 months:
    https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey=demo

    Querying all the earnings events for IBM in the next 12 months:
    https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&symbol=IBM&horizon=12month&apikey=demo
    """
    csv_url = URL + f'EARNINGS_CALENDAR&horizon={horizon}&apikey={API_KEY}'
    df = csv_request(csv_url=csv_url)

    return df


def ipo_calendar():
    """
    returns a list of IPOs expected in the next 3 months.

    Examples
    To ensure optimal API response time, this endpoint uses the CSV format which is more memory-efficient than JSON.

    Querying all the company earnings expected in the next 3 months:
    https://www.alphavantage.co/query?function=IPO_CALENDAR&apikey=demo
    """
    csv_url = URL + f'IPO_CALENDAR&apikey={API_KEY}'
    df = csv_request(csv_url=csv_url)

    return df
