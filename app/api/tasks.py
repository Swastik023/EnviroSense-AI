from app import celery
from app.api.openweather import get_weather
from app.api.airvisual import get_air_quality
from app.api.nrel import get_energy_data
from app.models.weather import Weather
from app.models.air_quality import AirQuality
from app.models.energy import Energy
from app import db

@celery.task
def update_data():
    # Fetch data from APIs
    weather_data = get_weather("New York")
    air_quality_data = get_air_quality("New York")
    energy_data = get_energy_data(40.7128, -74.0060)

    # Process and save data to the database
    with db.session.begin():
        weather_entry = Weather(
            city=weather_data['name'],
            temperature=weather_data['main']['temp'],
            humidity=weather_data['main']['humidity'],
            description=weather_data['weather'][0]['description']
        )
        air_quality_entry = AirQuality(
            city=air_quality_data['data']['city'],
            aqi=air_quality_data['data']['current']['pollution']['aqius'],
            pm25=air_quality_data['data']['current']['pollution']['aqius_pm25'],
            pm10=air_quality_data['data']['current']['pollution']['aqius_pm10'],
            co=air_quality_data['data']['current']['pollution']['aqius_co'],
            no2=air_quality_data['data']['current']['pollution']['aqius_no2'],
            o3=air_quality_data['data']['current']['pollution']['aqius_o3']
        )
        energy_entry = Energy(
            lat=40.7128,
            lon=-74.0060,
            solar=energy_data['outputs']['avg_dni'],
            wind=energy_data['outputs']['avg_windspeed']
        )

        db.session.add(weather_entry)
        db.session.add(air_quality_entry)
        db.session.add(energy_entry)
