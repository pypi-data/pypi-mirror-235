import requests
import pandas as pd
import csv

API_KEY = "demo"  # change to your API_KEY
URL = "https://www.alphavantage.co/query?function="


def easy_request(easy_url: str):
    response = requests.get(easy_url).json()

    return response


def csv_request(csv_url: str) -> pd.DataFrame:
    with requests.Session() as s:
        download = s.get(csv_url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)

    df = pd.DataFrame(my_list[1:], columns=my_list[0])

    return df


def dataframe_request(url: str) -> pd.DataFrame:
    response = easy_request(easy_url=url)

    return pd.DataFrame(response["data"])
