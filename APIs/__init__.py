import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    API_KEY = os.getenv("API_KEY")

    print(API_KEY)