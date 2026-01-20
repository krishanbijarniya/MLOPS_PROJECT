import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

def check_drift(reference_data: pd.DataFrame, current_data: pd.DataFrame) -> bool:
    print("Generating Evidently drift report...")
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference_data, current_data=current_data)
    
    # Parse result (mock logic)
    drift_detected = False
    print(f"Drift check completed. Drift detected: {drift_detected}")
    return drift_detected

if __name__ == "__main__":
    ref = pd.DataFrame({"price": [10, 20, 30]})
    curr = pd.DataFrame({"price": [12, 19, 29]})
    check_drift(ref, curr)
