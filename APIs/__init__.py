import os
import json
from dotenv import load_dotenv

from NewsApiRequests import NewsApiRequests

if __name__ == "__main__":
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    NEWS_TOPIC = os.getenv("NEWS_TOPIC", "cats")
    
    if API_KEY == None:
        raise ValueError("No API_KEY value found in environment variables. Use a .env file and add an API_KEY value. See README.")
    
    api_requests = NewsApiRequests(API_KEY)

    response = api_requests.get(NEWS_TOPIC)

    print(json.dumps(response, indent=2))