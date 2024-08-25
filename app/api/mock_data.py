def get_mock_weather():
    return {
        "coord": {"lon": -0.1257, "lat": 51.5085},
        "weather": [{"description": "clear sky"}],
        "main": {"temp": 15.0, "humidity": 65},
        "name": "London"
    }

def get_mock_air_quality():
    return {
        "data": {
            "city": "London",
            "current": {"pollution": {"aqius": 42}}
        }
    }

def get_mock_energy_data():
    return {
        "outputs": {
            "avg_dni": 4.5,
            "avg_windspeed": 5.2
        }
    }
