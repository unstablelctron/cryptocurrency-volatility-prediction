from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("xgb_volatility_model.pkl")

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert JSON to DataFrame
    df = pd.DataFrame([data])

    # Predict logATR
    logatr_pred = model.predict(df)[0]

    # Convert to actual ATR
    atr_pred = float(np.exp(logatr_pred))

    return jsonify({
        "logATR": float(logatr_pred),
        "ATR": atr_pred
    })


if __name__ == '__main__':
    app.run(debug=True)
