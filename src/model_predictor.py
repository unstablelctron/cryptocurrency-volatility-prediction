import os
import pickle
from typing import Union

import pandas as pd

# Path to the trained XGBoost model
MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "xgb_volatility_model.pkl",
)


def load_model(path: str = MODEL_PATH):
    """Load and return the trained model from disk."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at: {path}")
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


def predict_volatility(model, features: Union[pd.DataFrame, dict, list]):
    """Run predictions using the provided model and input features.

    Parameters
    ----------
    model:
        Trained model with a .predict() method (e.g. XGBRegressor).
    features:
        Either:
        - a pandas DataFrame, or
        - a dict representing a single row, or
        - a list of dicts representing multiple rows.

    Returns
    -------
    np.ndarray
        Array of predictions.
    """
    if isinstance(features, dict):
        features = pd.DataFrame([features])
    elif isinstance(features, list):
        features = pd.DataFrame(features)

    return model.predict(features)
