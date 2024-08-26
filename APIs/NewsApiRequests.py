import requests
from typing import LiteralString

class NewsApiRequests:
    def __init__(self, api_key) -> None:
        self.__api_host__ =  f"https://newsapi.org/v2/everything?apiKey={api_key}"
        pass

    def get(self, query_string: LiteralString, from_date: LiteralString = "2024-08-01", to_date: LiteralString = "2024-08-24"):
        url = self.__api_host__ + f"&qInTitle={query_string}&from={from_date}&to={to_date}"
        response = requests.get(url)

        return response.json()