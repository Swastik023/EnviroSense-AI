from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.config.Config')

# Initialize the database
db = SQLAlchemy(app)

# Import and register blueprints
from app.dashboard.views import bp as dashboard_bp
app.register_blueprint(dashboard_bp)

if __name__ == '__main__':
    app.run(debug=True)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

celery = make_celery(app)
