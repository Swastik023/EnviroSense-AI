from ml.forecasting_model import train_model
from ml.data_preprocessing import preprocess_data

def train_forecast_model(data):
    df = preprocess_data(data)
    X = df[['feature1', 'feature2']]  # Replace with actual features
    y = df['target']  # Replace with actual target
    model = train_model(X, y)
    return model
