from settings import *


def commodities_prices(function="WTI", interval="monthly"):
    """
    ❚ Optional: function
    accept: [WTI, BRENT, NATURAL_GAS, COPPER, ALUMINUM, WHEAT, CORN, COTTON, SUGAR, COFFEE]

    ❚ Optional: interval
    By default, interval=monthly. Strings daily, weekly, and monthly are accepted.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=WTI&interval=monthly&apikey=demo
    """

    url = URL + f"{function}&interval={interval}&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def global_commodities_index(interval="monthly"):
    """
    returns the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.

    Source: International Monetary Fund (IMF Terms of Use), Global Price Index of All Commodities, retrieved from FRED,
    Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is not endorsed or certified by the Federal
    Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the FRED® API Terms of Use.

    ❚ Optional: interval
    By default, interval=monthly. Strings monthly, quarterly, and annual are accepted.
    """
    url = URL + f"ALL_COMMODITIES&interval={interval}&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df
