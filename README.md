
# EnviroSense-AI

## Project Overview

**EnviroSense-AI** is an advanced tool designed to aggregate and analyze environmental data from multiple public APIs. The tool provides real-time insights and forecasts based on weather conditions, air quality, and energy consumption data, making it a valuable resource for researchers, urban planners, environmental agencies, and the general public.

## Features

- **API Integration**: Aggregates data from OpenWeatherMap, AirVisual, and NREL.
- **Data Management**: Stores data in an SQLite database using SQLAlchemy.
- **Machine Learning-Based Forecasting**: Predicts future environmental trends.
- **Interactive Analytics Dashboard**: Visualizes aggregated data and forecasts.
- **Automated Data Updates**: Periodically fetches and updates data automatically.
- **Dockerization**: Containerized application for easy deployment.
- **Deployment on Heroku and GitHub Pages**: Deploys both backend and static frontend.

## Project Structure and File Descriptions

### **Directory Structure**

```
EnviroSense-AI/
│
├── app/
│   ├── __init__.py          # Initializes the Flask application and SQLAlchemy database
│   ├── api/                 # Contains API integration modules
│   │   ├── openweather.py   # Fetches weather data from OpenWeatherMap API
│   │   ├── airvisual.py     # Fetches air quality data from AirVisual API
│   │   ├── nrel.py          # Fetches renewable energy data from NREL API
│   │   └── mock_data.py     # Provides mock data for testing without hitting live APIs
│   └── dashboard/
│       ├── views.py         # Defines the routes and logic for the interactive dashboard
│       ├── templates/       # Contains HTML templates for the dashboard
│       │   └── dashboard.html # Main HTML file for displaying the dashboard
│
├── config/
│   ├── config.py            # Configuration settings for Flask and API keys
│   ├── credentials.py       # Stores API keys securely (add yours here)
│
├── models/
│   ├── weather.py           # SQLAlchemy model for storing weather data
│   ├── air_quality.py       # SQLAlchemy model for storing air quality data
│   └── energy.py            # SQLAlchemy model for storing energy data
│
├── ml/
│   ├── forecasting_model.py # Contains the machine learning model for forecasting
│   ├── data_preprocessing.py# Preprocessing scripts for preparing data for ML models
│   └── model_training.py    # Handles the training of the machine learning model
│
├── static/
│   ├── css/                 # CSS files for styling the dashboard
│   ├── js/                  # JavaScript files for dashboard interactivity
│   └── images/              # Image assets for the dashboard
│
├── templates/
│   ├── base.html            # Base HTML template that other templates extend
│   ├── index.html           # Landing page HTML for the application
│
├── tests/
│   ├── test_api.py          # Unit tests for the API integration modules
│   └── test_dashboard.py    # Unit tests for the dashboard routes and views
│
├── Dockerfile               # Dockerfile for containerizing the application
├── docker-compose.yml       # Docker Compose file for setting up multi-container environments
├── requirements.txt         # Python dependencies required for the project
├── README.md                # Project documentation (this file)
└── run.py                   # Entry point for running the Flask application
```

### **How the Project is Structured and Connected**

1. **Flask Application Setup (`app/__init__.py`)**:
   - This file initializes the Flask application and sets up the SQLAlchemy database. It loads configuration settings from `config/config.py` and registers the dashboard blueprint from `app/dashboard/views.py`.

2. **API Integration (`app/api/`)**:
   - Contains modules for fetching data from various APIs:
     - `openweather.py`: Interacts with the OpenWeatherMap API to get current weather data.
     - `airvisual.py`: Fetches air quality data from the AirVisual API.
     - `nrel.py`: Retrieves solar and wind energy data from the National Renewable Energy Laboratory (NREL) API.
     - `mock_data.py`: Provides mock data for testing purposes without using live API calls.

3. **Dashboard (`app/dashboard/`)**:
   - `views.py`: Contains Flask routes for rendering the interactive analytics dashboard. It fetches data from the APIs or database and sends it to the HTML templates for rendering.
   - `templates/dashboard.html`: The main HTML file that displays the data on the dashboard using Jinja2 templating. It shows weather, air quality, and energy data.

4. **Configuration (`config/`)**:
   - `config.py`: Contains general configuration settings for Flask, such as database URI and API keys.
   - `credentials.py`: A separate file to securely store API keys. You should add your API keys here.

5. **Data Models (`models/`)**:
   - SQLAlchemy models that define the structure of the data stored in the SQLite database:
     - `weather.py`: Defines the schema for weather data.
     - `air_quality.py`: Defines the schema for air quality data.
     - `energy.py`: Defines the schema for energy data.

6. **Machine Learning (`ml/`)**:
   - Scripts for machine learning model development and data preprocessing:
     - `forecasting_model.py`: Contains the machine learning model for forecasting future environmental trends.
     - `data_preprocessing.py`: Preprocesses the data fetched from APIs for use in machine learning models.
     - `model_training.py`: Handles the training and evaluation of the machine learning model.

7. **Static and Templates Directories**:
   - `static/`: Contains static files like CSS, JavaScript, and images used for styling and enhancing the dashboard's interactivity.
   - `templates/`: Contains HTML templates that the Flask app renders. `base.html` is a base template extended by other HTML files.

8. **Testing (`tests/`)**:
   - `test_api.py` and `test_dashboard.py`: Include unit tests for testing the API integrations and dashboard routes, ensuring that the application behaves as expected.

9. **Dockerization**:
   - `Dockerfile`: A script that Docker uses to create an image of your application. It installs Python, copies your project files into the image, installs dependencies, and specifies the command to run your Flask app.
   - `docker-compose.yml`: Defines a Docker service for your Flask app, making it easier to run with Docker Compose. This file sets up the application environment, including ports and environment variables.

10. **Project Initialization and Execution (`run.py`)**:
   - `run.py`: The entry point for starting the Flask application. When you run this file, it starts the Flask development server and serves the application.

## Installation

### Prerequisites

- Python 3.x
- Git
- Docker (optional, for containerization)
- Heroku CLI (for deployment)

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Swastik023/EnviroSense-AI.git
cd EnviroSense-AI
```

### Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv env
env\Scripts\activate  # On Windows
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application Locally

1. **Set up environment variables**: Add your API keys to `config/credentials.py`.
2. **Initialize the database**:

   ```bash
   python
   ```

   ```python
   from app import app, db
   with app.app_context():
       db.create_all()
   exit()
   ```

3. **Run the Flask Application**:

   ```bash
   python run.py
   ```

4. Open your web browser and go to `http://localhost:5000` to access the dashboard.

## API Endpoints

### Weather Data

- **Endpoint**: `/api/weather`
- **Method**: GET
- **Description**: Retrieves current weather data for a specified location.

### Air Quality Data

- **Endpoint**: `/api/airquality`
- **Method**: GET
- **Description**: Retrieves air quality index (AQI) for a specified location.

### Energy Data

- **Endpoint**: `/api/energy`
- **Method**: GET
- **Description**: Retrieves renewable energy data based on geographic coordinates.

## Data Sources

1. **OpenWeatherMap**: Provides weather data such as temperature, humidity, wind speed, etc.
2. **AirVisual**: Offers air quality data including AQI and pollutant levels.
3. **National Renewable Energy Laboratory (NREL)**: Supplies solar and wind energy data.

## Machine Learning

The project uses a machine learning model to forecast environmental trends. The model is built using Scikit-Learn and is trained on historical data aggregated from the APIs.

### Training the Model

To train the model, run:

```bash
python ml/model_training.py
```

## Deployment

### Deploying to Heroku

1. **Login to Heroku**:



   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:

   ```bash
   heroku create enviro-sense-ai
   ```

3. **Deploy the app**:

   ```bash
   git push heroku main
   ```

4. **Open your app**:

   ```bash
   heroku open
   ```

### Deploying Static Frontend to GitHub Pages

1. Go to your GitHub repository settings.
2. Under **GitHub Pages**, set the source to the `main` branch and save.
3. Visit `https://<your-username>.github.io/EnviroSense-AI/` to view your frontend.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to OpenWeatherMap, AirVisual, and NREL for providing free API access.
- Inspiration and guidance from open-source contributors and community.
```

### **Summary**

This enhanced README provides a comprehensive overview of the project, detailing each file's purpose and how different parts of the project are interconnected. It also offers setup instructions, deployment steps, and a clear structure for contributors to follow. 

Feel free to modify the README further to fit the specifics of your project. Let me know if you need any more adjustments or have other questions!
