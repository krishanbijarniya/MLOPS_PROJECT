# Retail Demand & Price Optimization Pipeline

This repository contains the end-to-end MLOps pipeline for predicting product demand and optimizing pricing strategies.

## Features
- Data versioning with DVC.
- Model experiment tracking and registry with MLflow.
- API serving via FastAPI.
- Continuous monitoring and drift detection with Evidently.ai.

## Running Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Training Pipeline
```bash
python src/pipelines/train.py
```

### 3. Run serving API
```bash
uvicorn src.serving.app:app --reload
```
