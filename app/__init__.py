from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

# Initialize Flask application
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.config.Config')

# Initialize the database
db = SQLAlchemy(app)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

# Update configuration for Celery
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

# Initialize Celery
celery = make_celery(app)

# Import and register blueprints after initializing app and other components
from dashboard.views import bp as dashboard_bp  # Import at the end to avoid circular imports
app.register_blueprint(dashboard_bp)
