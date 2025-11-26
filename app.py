from flask import Flask, request, jsonify, render_template
import pandas as pd
import traceback

from src.model_predictor import load_model, predict_volatility
from src.utils import ensure_feature_order
from src.config import FEATURE_COLUMNS

app = Flask(__name__)

# Load model once at startup
try:
    model = load_model()
except Exception as e:
    # In production you would log this properly
    print("Error loading model at startup:", e)
    model = None


@app.route("/")
def index():
    """Simple home page with basic instructions."""
    return render_template("index.html", feature_columns=FEATURE_COLUMNS)


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """Accept JSON and return model predictions.

    Expected formats:
    - Single record (JSON object)
    - Multiple records (JSON array of objects)
    """
    if model is None:
        return jsonify({"error": "Model not loaded on server."}), 500

    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "No JSON payload received."}), 400

        # Convert to DataFrame
        if isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            df = pd.DataFrame(data)

        # Match required feature order
        df = ensure_feature_order(df)

        preds = predict_volatility(model, df)
        return jsonify({"predictions": preds.tolist()})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # For local development only
    app.run(host="0.0.0.0", port=5000, debug=True)
