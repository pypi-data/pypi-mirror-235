from .settings import *


def real_gdp(interval="annual"):
    """
    returns the annual and quarterly Real GDP of the United States.

    Source: U.S. Bureau of Economic Analysis, Real Gross Domestic Product, retrieved from FRED,
    Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is not endorsed or certified by
    the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the FRED® API Terms of Use.

    ❚ Optional: interval
    By default, interval=annual. Strings quarterly and annual are accepted.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=demo

    Tips: The generated data is in billion units
    """
    url = URL + f"REAL_GDP&interval={interval}&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def real_gdp_per_capita():
    """
    returns the quarterly Real GDP per Capita data of the United States.

    Source: U.S. Bureau of Economic Analysis, Real gross domestic product per capita, retrieved from FRED,
    Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is not endorsed or certified by
    the Federal Reserve Bank of St. Louis. By using this data feed, you agree to be bound by the FRED® API Terms of Use.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey=demo
    """

    url = URL + f"REAL_GDP_PER_CAPITA&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def treasury_yield(interval="monthly", maturity="10year"):
    """
    returns the daily, weekly, and monthly US treasury yield of a given maturity timeline (e.g., 5 year, 30 year, etc).

    Source: Board of Governors of the Federal Reserve System (US), Market Yield on U.S. Treasury Securities at
    3-month, 2-year, 5-year, 7-year, 10-year, and 30-year Constant Maturities, Quoted on an Investment Basis,
    retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API but is not endorsed
    or certified by the Federal Reserve Bank of St. Louis. By using this data feed,
    you agree to be bound by the FRED® API Terms of Use.

    ❚ Optional: interval
    By default, interval=monthly. Strings daily, weekly, and monthly are accepted.

    ❚ Optional: maturity
    By default, maturity=10year. Strings 3month, 2year, 5year, 7year, 10year, and 30year are accepted.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey=demo
    """
    url = URL + f"TREASURY_YIELD&interval={interval}&maturity={maturity}&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def federal_funds_ratio(interval="monthly"):
    """
    returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.

    Source: Board of Governors of the Federal Reserve System (US), Federal Funds Effective Rate, retrieved from FRED,
    Federal Reserve Bank of St. Louis (https://fred.stlouisfed.org/series/FEDFUNDS). This data feed uses the FRED® API
    but is not endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed,
    you agree to be bound by the FRED® API Terms of Use.

    ❚ Optional: interval
    By default, interval=monthly. Strings daily, weekly, and monthly are accepted.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval=monthly&apikey=demo
    """
    url = URL + f"FEDERAL_FUNDS_RATE&interval={interval}&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def cpi(interval="monthly"):
    """
    returns the monthly and semiannual consumer price index (CPI) of the United States.
    CPI is widely regarded as the barometer of inflation levels in the broader economy.

    Source: U.S. Bureau of Labor Statistics, Consumer Price Index for All Urban Consumers: All Items in U.S.
    City Average, retrieved from FRED, Federal Reserve Bank of St. Louis. This data feed uses the FRED® API
    but is not endorsed or certified by the Federal Reserve Bank of St. Louis. By using this data feed,
    you agree to be bound by the FRED® API Terms of Use.

    ❚ Optional: interval
    By default, interval=monthly. Strings monthly and semiannual are accepted.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=demo
    """
    url = URL + f"CPI&interval={interval}&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def usa_inflation():
    """
    returns the annual inflation rates (consumer prices) of the United States.

    Source: World Bank, Inflation, consumer prices for the United States, retrieved from FRED, Federal Reserve Bank
    of St. Louis. This data feed uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank
    of St. Louis. By using this data feed, you agree to be bound by the FRED® API Terms of Use.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=INFLATION&apikey=demo
    """
    url = URL + f"INFLATION&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def retail_sales():
    """
    returns the monthly Advance Retail Sales: Retail Trade data of the United States.

    Source: U.S. Census Bureau, Advance Retail Sales: Retail Trade, retrieved from FRED, Federal Reserve Bank of
    St. Louis (https://fred.stlouisfed.org/series/RSXFSN). This data feed uses the FRED® API but is not endorsed or
    certified by the Federal Reserve Bank of St. Louis. By using this data feed,
    you agree to be bound by the FRED® API Terms of Use.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=RETAIL_SALES&apikey=demo
    """
    url = URL + f"RETAIL_SALES&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def durable_goods_orders():
    """
    returns the monthly manufacturers' new orders of durable goods in the United States.

    Source: U.S. Census Bureau, Manufacturers' New Orders: Durable Goods, retrieved from FRED, Federal Reserve Bank
    of St. Louis (https://fred.stlouisfed.org/series/UMDMNO). This data feed uses the FRED® API but is not endorsed
    or certified by the Federal Reserve Bank of St. Louis. By using this data feed,
    you agree to be bound by the FRED® API Terms of Use.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=DURABLES&apikey=demo
    """
    url = URL + f"DURABLES&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def unemployment_rate():
    """
    returns the monthly unemployment data of the United States. The unemployment rate represents the number of
    unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older,
    who currently reside in 1 of the 50 states or the District of Columbia,
    who do not reside in institutions (e.g., penal and mental facilities, homes for the aged),
    and who are not on active duty in the Armed Forces (source).

    Source: U.S. Bureau of Labor Statistics, Unemployment Rate, retrieved from FRED, Federal Reserve Bank of St. Louis.
    This data feed uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis.
    By using this data feed, you agree to be bound by the FRED® API Terms of Use.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey=demo
    """
    url = URL + f"UNEMPLOYMENT&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df


def nonfarm_payroll():
    """
    returns the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), a measure of
    the number of U.S. workers in the economy that excludes proprietors, private household employees,
    unpaid volunteers, farm employees, and the unincorporated self-employed.

    Source: U.S. Bureau of Labor Statistics, All Employees, Total Nonfarm, retrieved from FRED, Federal Reserve Bank
    of St. Louis. This data feed uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank
    of St. Louis. By using this data feed, you agree to be bound by the FRED® API Terms of Use.

    Examples (click for JSON output)
    https://www.alphavantage.co/query?function=NONFARM_PAYROLL&apikey=demo
    """

    url = URL + f"NONFARM_PAYROLL&apikey={API_KEY}"
    data_df = dataframe_request(url=url)

    return data_df
