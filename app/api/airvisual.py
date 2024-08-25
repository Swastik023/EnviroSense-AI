import requests
from flask import current_app

def get_air_quality(city):
    api_key = current_app.config['AIRVISUAL_API_KEY']
    base_url = f"https://api.airvisual.com/v2/city?city={city}&key={api_key}"
    response = requests.get(base_url)
    return response.json()
