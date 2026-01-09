import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import mlflow
import mlflow.sklearn
from ingest import ingest_data, preprocess_data

def train_model():
    df = ingest_data("dummy_path")
    df = preprocess_data(df)
    
    X = df[['price', 'competitor_price', 'day_of_week', 'price_difference']]
    y = df['demand']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    mlflow.set_experiment("Retail_Demand_Optimization")
    
    with mlflow.start_run():
        n_estimators = 100
        max_depth = 10
        
        rf = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        rf.fit(X_train, y_train)
        
        # Log params
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        
        # Log metrics
        train_score = rf.score(X_train, y_train)
        test_score = rf.score(X_test, y_test)
        mlflow.log_metric("train_r2", train_score)
        mlflow.log_metric("test_r2", test_score)
        
        # Log model
        mlflow.sklearn.log_model(rf, "model")
        print(f"Model trained successfully. Test R2: {test_score:.4f}")

if __name__ == "__main__":
    train_model()
