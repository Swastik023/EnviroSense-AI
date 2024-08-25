import requests
from flask import current_app

def get_energy_data(latitude, longitude):
    if current_app.config['USE_DUMMY_DATA']:
        # Dummy data for demonstration purposes
        energy_data = {
            'solar': 200,  # Solar energy in kWh/m^2/year
            'wind': 150,  # Wind energy in kWh/m^2/year
            'geothermal': 120,  # Geothermal energy in kWh/m^2/year
        }
        return energy_data

    # Original API code remains unchanged
    api_key = "your_nrel_api_key"  # Replace with your actual API key
    base_url = f"https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={api_key}&lat={latitude}&lon={longitude}"

    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        energy_data = {
            'solar': data['outputs']['avg_dni']['annual'],
            'wind': data.get('wind_speed', {}).get('annual')  # Adjust this line based on actual API response
        }
        return energy_data
    else:
        print("Failed to fetch energy data")
        return None
