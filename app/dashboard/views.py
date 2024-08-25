from flask import Blueprint, render_template
from app.api.openweather import get_weather
from app.api.airvisual import get_air_quality
from app.api.nrel import get_energy_data

# Define the Blueprint
bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    city = "New York"
    weather_data = get_weather(city)
    air_quality_data = get_air_quality(city)
    energy_data = get_energy_data(40.7128, -74.0060)  # Example: New York coordinates
    return render_template('dashboard.html', weather=weather_data, air_quality=air_quality_data, energy=energy_data)
