import requests
from flask import current_app

def get_energy_data(lat, lon):
    api_key = current_app.config['NREL_API_KEY']
    base_url = f"https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={api_key}&lat={lat}&lon={lon}"
    response = requests.get(base_url)
    return response.json()
