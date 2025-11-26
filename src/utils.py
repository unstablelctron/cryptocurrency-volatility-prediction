import pandas as pd
from .config import FEATURE_COLUMNS


def ensure_feature_order(df: pd.DataFrame) -> pd.DataFrame:
    """Reorder and subset dataframe to match FEATURE_COLUMNS.

    Raises:
        KeyError: if any required feature is missing.
    """
    missing = [c for c in FEATURE_COLUMNS if c not in df.columns]
    if missing:
        raise KeyError(f"Missing required feature columns: {missing}")
    return df[FEATURE_COLUMNS]
