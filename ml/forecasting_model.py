from sklearn.ensemble import RandomForestRegressor

def train_model(X, y):
    """Train a machine learning model."""
    model = RandomForestRegressor()  # Using a RandomForest model as an example
    model.fit(X, y)
    return model
