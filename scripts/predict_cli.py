"""Simple CLI script to test the trained model with a sample row."""
import sys
import os

# Add project root to sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)



import json
import pandas as pd

from src.model_predictor import load_model, predict_volatility
from src.utils import ensure_feature_order
from src.config import FEATURE_COLUMNS


def main():
    model = load_model()

    # Example input row
    example = {
        "open": 51.37,
        "high": 57.85,
        "low": 49.62,
        "close": 51.31,
        "volume": 3132405,
        "marketCap": 123456789,
        "tr": 2.31,
        "log_return": -0.0123,
        "Day": 15,
        "Month": 5,
        "Year": 2024,
        "crypto_name_encoded": 0
    }

    df = pd.DataFrame([example])
    df = ensure_feature_order(df)

    preds = predict_volatility(model, df)
    print("Input row:")
    print(json.dumps(example, indent=2))
    print("\nPrediction:", preds[0])


if __name__ == "__main__":
    main()
