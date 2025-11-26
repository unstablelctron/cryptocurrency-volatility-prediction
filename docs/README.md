# 🚀 Crypto Volatility Prediction  
**End-to-End Machine Learning Project using XGBoost**

This project predicts cryptocurrency volatility using historical OHLC data and engineered technical indicators.  
The model uses **XGBoost Regression** to predict **log(ATR14)** — a widely used volatility measure.

# 📂 Project Structure

Crypto-Volatility-Predictor/
│── app.py # Flask API for predictions
│── src/
│ ├── model_predictor.py # Model loader + predictor
│ ├── utils.py # Helper functions
│ ├── config.py # Feature columns & paths
│── models/
│ └── xgb_volatility_model.pkl
│── scripts/
│ └── predict_cli.py # CLI test script
│── notebooks/
│ └── crypto_volatility_end_to_end.ipynb
│── templates/
│ └── index.html # Documentation UI for API
│── config/
│ └── model_selection.yaml
│ └── training_schema.json
│── data/
│── docs/
│── requirements.txt
│── README.md


---

# 🎯 Project Objective

Cryptocurrency markets are highly volatile.  
This project aims to **estimate future volatility** using machine learning by predicting:

target = log(atr_14)


Volatility metrics like ATR help in:

- Risk management  
- Trading strategy  
- Portfolio balancing  
- Algo-trading pipelines  

---

# 📊 Dataset Features

Final model uses **12 input features**:

| Feature |
|---------|
| open |
| high |
| low |
| close |
| volume |
| marketCap |
| tr |
| log_return |
| crypto_name_encoded |
| Day |
| Month |
| Year |

Target variable:

target = log(atr_14)


ATR14 & crypto_name are removed during inference.

---

# 🧠 Feature Engineering Performed

- `tr = high - low`  
- `log_return = ln(close / close.shift(1))`  
- `atr_14 = tr.rolling(14).mean()`  
- Label encoding for crypto name  
- Date → Day, Month, Year  
- Final target → log(atr_14)

---

# 🏗 Model Details (XGBoost Regressor)

Final model was trained with:

```python
n_estimators = 600
learning_rate = 0.01
max_depth = 4
subsample = 0.7
colsample_bytree = 0.6
tree_method = "hist"

Test Metrics:

RMSE: ~3.57

MAE: ~39

R² Score: ~0.67

Model saved as:
models/xgb_volatility_model.pkl


🌐 API Usage (Flask)
Start the API:
python app.py
🔥 Endpoint
POST /api/predict
Headers
Content-Type: application/json

Example JSON body
{
  "open": 51.37,
  "high": 57.85,
  "low": 49.62,
  "close": 51.31,
  "volume": 3132405,
  "marketCap": 123456789,
  "tr": 2.31,
  "log_return": -0.0123,
  "crypto_name_encoded": 0,
  "Day": 15,
  "Month": 5,
  "Year": 2024
}
Example Response:
{
  "predictions": [1.3547]
}


🖥 CLI Prediction Script


python scripts/predict_cli.py
Outputs model prediction for a sample row.

📝 How to Train / Experiment

All EDA, feature engineering, model selection, and training steps are documented in:

notebooks/crypto_volatility_end_to_end.ipynb

🎉 Conclusion

This project provides:

Full end-to-end ML pipeline

Clean feature engineering & transformations

Reproducible model

API for real-time predictions

CLI interface

Production-ready folder structure

Ideal for:

GitHub portfolios

ML deployment demos

Interviews

Crypto research

Algo-trading prototypes

Created by Anand Pathak