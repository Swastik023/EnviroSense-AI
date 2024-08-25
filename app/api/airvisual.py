import requests
from flask import current_app

def get_air_quality(city):
    if current_app.config['USE_DUMMY_DATA']:
        # Dummy data for demonstration purposes
        air_quality_data = {
            'aqi': 50,  # Air Quality Index
            'main_pollutant': 'PM2.5',  # Main pollutant
            'advice': 'Air quality is considered satisfactory.'  # Example advisory message
        }
        return air_quality_data

    # Original API code remains unchanged
    api_key = "your_airvisual_api_key"  # Replace with your actual API key
    base_url = f"http://api.airvisual.com/v2/city?city={city}&key={api_key}"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        air_quality_data = {
            'aqi': data['data']['current']['pollution']['aqius'],
            'main_pollutant': data['data']['current']['pollution']['mainus']
        }
        return air_quality_data
    else:
        print("Failed to fetch air quality data")
        return None
