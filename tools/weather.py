import os
import requests

from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city.

    Args:
        city: Name of the city.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Could not get weather for {city}"

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    return (
        f"Weather in {city}: "
        f"{temperature}°C, "
        f"{description}, "
        f"humidity {humidity}%"
    )