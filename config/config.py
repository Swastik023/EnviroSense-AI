import os
from config.credentials import Credentials

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///environmental_data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENWEATHER_API_KEY = Credentials.OPENWEATHER_API_KEY
    AIRVISUAL_API_KEY = Credentials.AIRVISUAL_API_KEY
    NREL_API_KEY = Credentials.NREL_API_KEY
