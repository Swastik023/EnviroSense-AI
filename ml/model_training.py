from ml.forecasting_model import train_model
from ml.data_preprocessing import preprocess_data

def train_forecast_model(data):
    # Preprocess the data
    df = preprocess_data(data)
    
    # Define features and target
    X = df[['temperature', 'humidity', 'wind_speed']]  # Simulated features
    y = df['energy_output']  # Simulated target
    
    # Train the model
    model = train_model(X, y)
    
    # Simulate output
    print("Model trained successfully!")
    print(f"Simulated model parameters: Coefficients - {model.feature_importances_}")  # Example output for RandomForest

    return model

if __name__ == "__main__":
    # Simulated data for training
    example_data = {
        'temperature': [25, 30, 20, 15, 10],  # in Celsius
        'humidity': [80, 70, 75, 85, 90],  # in percentage
        'wind_speed': [5, 7, 3, 8, 10],  # in m/s
        'energy_output': [200, 250, 150, 180, 220]  # Simulated energy output in kWh
    }
    
    # Train the forecasting model with simulated data
    model = train_forecast_model(example_data)
