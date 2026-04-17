import requests
from config import API_QUERY_STRING

url = "https://api.tomorrow.io/v4/weather/history/recent"

def get_weather_data():
    hourly = []

    headers = {
        "accept-encoding": "deflate, gzip, br",
        "accept": "application/json"
    }
    params = {
        "location": "nairobi",
        "apikey": API_QUERY_STRING
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        nairobi_weather_data = response.json()
        hourly = nairobi_weather_data.get("timelines", {}).get("hourly", [])

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while collecting data: {e}")


    return hourly