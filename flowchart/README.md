## 🔄 Crypto Volatility Prediction – Exact Model Pipeline

```mermaid
flowchart TD

A[Raw Crypto Price Data<br/>open, high, low, close, volume, marketCap, date] --> B[Feature Engineering]

B --> B1[Compute TR = high - low]
B --> B2[Compute log_return = ln(close/prev_close)]
B --> B3[Label Encode crypto_name → crypto_name_encoded]
B --> B4[Extract Day, Month, Year from date]
B --> B5[Compute ATR14 → log(ATR14)]
B --> C[Form Final Dataset]

C --> C1[DROP atr_14]
C --> C2[DROP crypto_name]

C1 --> D[Final 12 Features]
C2 --> D

D --> E[Train-Test Split]

E --> F[Train XGBoost Regressor<br/>with tuned params]
F --> G[Evaluate Model<br/>RMSE, MAE, R²]

G --> H[SAVE MODEL<br/>xgb_volatility_model.pkl]

H --> I[Load Model in Flask API]

I --> J[POST /api/predict<br/>Accept 12 Features Only]

J --> K[Model Predicts target<br/>= log(ATR14)]

