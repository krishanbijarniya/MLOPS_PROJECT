import pandas as pd
import numpy as np

def ingest_data(file_path: str) -> pd.DataFrame:
    print(f"Loading data from {file_path}")
    # Dummy data generation for simulation
    np.random.seed(42)
    n_samples = 1000
    data = {
        'product_id': np.random.randint(1, 10, n_samples),
        'price': np.random.uniform(5.0, 100.0, n_samples),
        'competitor_price': np.random.uniform(4.0, 110.0, n_samples),
        'day_of_week': np.random.randint(0, 7, n_samples),
        'demand': np.random.randint(10, 500, n_samples)
    }
    df = pd.DataFrame(data)
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Preprocessing data")
    df['price_difference'] = df['competitor_price'] - df['price']
    return df

if __name__ == "__main__":
    df = ingest_data("dummy_path")
    df = preprocess_data(df)
    print(df.head())
