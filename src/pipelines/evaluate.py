import mlflow
import numpy as np

def evaluate_challenger_model(challenger_metric: float, threshold: float = 0.5):
    print(f"Evaluating challenger model. Score: {challenger_metric}")
    # Dummy champion logic
    champion_metric = 0.60
    if challenger_metric > champion_metric + threshold:
        print("Promotion approved: Challenger outperforms Champion.")
        return True
    else:
        print("Promotion rejected: Challenger underperforms.")
        return False

if __name__ == "__main__":
    evaluate_challenger_model(0.75)
