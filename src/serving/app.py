from fastapi import FastAPI
from pydantic import BaseModel
import json
from datetime import datetime

app = FastAPI(title="Demand Prediction API")

class PredictionInput(BaseModel):
    price: float
    competitor_price: float
    day_of_week: int

@app.get("/")
def read_root():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: PredictionInput):
    price_diff = data.competitor_price - data.price
    predicted_demand = max(10, int(200 - 2.5 * data.price + 1.5 * price_diff))
    
    # Log to file for drift analysis
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "price": data.price,
        "competitor_price": data.competitor_price,
        "day_of_week": data.day_of_week,
        "prediction": predicted_demand
    }
    with open("prediction_logs.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
        
    return {"predicted_demand": predicted_demand}
