# Crypto Volatility Predictor

End-to-end machine learning project for predicting cryptocurrency volatility using a trained XGBoost model.

## Project Structure

- `app.py`                – Flask API for online predictions
- `src/`                  – Source code (model loading, prediction utilities, configs)
- `models/`               – Saved trained model (`xgb_volatility_model.pkl`)
- `scripts/`              – CLI helpers (prediction, etc.)
- `config/`               – Configuration files (e.g. params, paths)
- `data/`                 – Raw and processed data 
- `notebooks/`            – Jupyter notebooks for EDA and experiments
- `templates/`            – HTML templates used by Flask
- `static/`               – Static assets (CSS, JS)
- `docs/`, `flowchart/`   – Documentation and diagrams

## Quickstart

1. Create and activate a virtual environment (recommended).
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python app.py
   ```

4. Send a POST request to the prediction endpoint:

   - URL: `http://127.0.0.1:5000/api/predict`
   - Method: `POST`
   - Body (JSON): one or more records that contain **exactly the same feature columns** used during training.

   Example :

   ```json
   {
     "open": 51.37,
     "high": 57.85,
     "low": 49.62,
     "close": 51.31,
     "volume": 3132405,
     "marketCap": 123456789,
     "tr": 2.31,
     "atr_14": 1.12,
     "log_return": -0.0123,
     "crypto_name_encoded": 0,
     "Day": 15,
     "Month": 5,
     "Year": 2024
   }
   ```

   or an array of such JSON objects.
