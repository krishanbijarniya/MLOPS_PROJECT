from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

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
    # Mock prediction model logic
    price_diff = data.competitor_price - data.price
    predicted_demand = max(10, int(200 - 2.5 * data.price + 1.5 * price_diff))
    return {"predicted_demand": predicted_demand}
