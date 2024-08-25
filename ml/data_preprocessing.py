import pandas as pd

def preprocess_data(data):
    df = pd.DataFrame(data)
    # Example: Drop missing values and normalize data
    df.dropna(inplace=True)
    return df
