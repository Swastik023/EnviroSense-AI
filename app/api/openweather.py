import requests
from flask import current_app

def get_weather(city):
    api_key = current_app.config['OPENWEATHER_API_KEY']
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()
