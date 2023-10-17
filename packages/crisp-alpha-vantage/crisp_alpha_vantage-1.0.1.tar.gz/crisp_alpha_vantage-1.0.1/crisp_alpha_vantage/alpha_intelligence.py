from settings import *


def market_news_senti(tickers="AAPL", limit=5) -> dict:
    """
    url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'

    Looking for market news data to train your LLM models or to augment your trading strategy?
    You have just found it. This API returns live and historical market news & sentiment data
    from a large & growing selection of premier news outlets around the world, covering stocks,
    cryptocurrencies, forex, and a wide range of topics such as fiscal policy, mergers &
    acquisitions, IPOs, etc. This API, combined with our core stock API, fundamental data,
    and technical indicator APIs, can provide you with a 360-degree view of the financial market
    and the broader economy.

    ❚ Optional: tickers
    The stock/crypto/forex symbols of your choice. For example: tickers=IBM will filter for articles that mention the IBM ticker; tickers=COIN,CRYPTO:BTC,FOREX:USD will filter for articles that simultaneously mention Coinbase (COIN), Bitcoin (CRYPTO:BTC), and US Dollar (FOREX:USD) in their content.

    ❚ Optional: topics
    The news topics of your choice. For example: topics=technology will filter for articles that write about the technology sector; topics=technology,ipo will filter for articles that simultaneously cover technology and IPO in their content. Below is the full list of supported topics:

    Blockchain: blockchain
    Earnings: earnings
    IPO: ipo
    Mergers & Acquisitions: mergers_and_acquisitions
    Financial Markets: financial_markets
    Economy - Fiscal Policy (e.g., tax reform, government spending): economy_fiscal
    Economy - Monetary Policy (e.g., interest rates, inflation): economy_monetary
    Economy - Macro/Overall: economy_macro
    Energy & Transportation: energy_transportation
    Finance: finance
    Life Sciences: life_sciences
    Manufacturing: manufacturing
    Real Estate & Construction: real_estate
    Retail & Wholesale: retail_wholesale
    Technology: technology

    ❚ Optional: time_from and time_to
    The time range of the news articles you are targeting, in YYYYMMDDTHHMM format. For example: time_from=20220410T0130. If time_from is specified but time_to is missing, the API will return articles published between the time_from value and the current time.

    ❚ Optional: sort
    By default, sort=LATEST and the API will return the latest articles first. You can also set sort=EARLIEST or sort=RELEVANCE based on your use case.

    ❚ Optional: limit
    By default, limit=50 and the API will return up to 50 matching results. You can also set limit=1000 to output up to 1000 results. If you are looking for an even higher output limit, please contact support@alphavantage.co to have your limit boosted.

    Examples (click for JSON output)
    Querying news articles that mention the AAPL ticker.
    https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo

    Querying news articles that simultaneously mention the Coinbase stock (COIN), Bitcoin (CRYPTO:BTC), and US Dollar (FOREX:USD) and are published on or after 2022-04-10, 1:30am UTC.
    https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=COIN,CRYPTO:BTC,FOREX:USD&time_from=20220410T0130&limit=1000&apikey=demo
    """

    easy_url = URL + f"NEWS_SENTIMENT&tickers={tickers}&limit={limit}&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response


def top_traded_tickers() -> dict:
    """
    url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'

    returns the top 20 gainers, losers, and the most active traded tickers in the US market.
    """
    easy_url = URL + f"TOP_GAINERS_LOSERS&apikey={API_KEY}"
    response = easy_request(easy_url=easy_url)

    return response
