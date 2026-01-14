from fastapi import FastAPI
app = FastAPI(title="Demand Prediction API")

@app.get("/")
def read_root():
    return {"status": "healthy"}
