import pandas as pd
import sys
sys.path.append("src/pipelines")
from ingest import ingest_data, preprocess_data

def test_ingestion():
    df = ingest_data("dummy")
    assert not df.empty
    assert "price" in df.columns

def test_preprocessing():
    df = pd.DataFrame({"price": [10], "competitor_price": [12]})
    df_proc = preprocess_data(df)
    assert df_proc["price_difference"].iloc[0] == 2
