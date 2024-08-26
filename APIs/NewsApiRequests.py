import requests

class NewsApiRequests:
    def __init__(self, api_key: str) -> None:
        self.__api_host__ =  f"https://newsapi.org/v2/everything?apiKey={api_key}"
        pass

    def get(self, query_string: str, from_date: str = "2024-08-01", to_date: str = "2024-08-24") -> dict:
        url = self.__api_host__ + f"&qInTitle={query_string}&from={from_date}&to={to_date}"
        response = requests.get(url)

        return response.json()