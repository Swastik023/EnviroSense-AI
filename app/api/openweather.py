import requests
from flask import current_app

def get_weather(city):
    if current_app.config['USE_DUMMY_DATA']:
        # Dummy data for demonstration purposes
        weather_data = {
            'temperature': 30,  # in Celsius
            'humidity': 70,  # in percentage
            'description': 'Clear sky',  # Weather description
            'wind_speed': 5  # in m/s
        }
        return weather_data

    # Original API code remains unchanged
    api_key = "your_openweather_api_key"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }
        return weather_data
    else:
        print("Failed to fetch weather data")
        return None
