# config/config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = 'your-secret-key'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    # Option to use dummy data instead of real API calls
    USE_DUMMY_DATA = True  # Set to False to use real API data
