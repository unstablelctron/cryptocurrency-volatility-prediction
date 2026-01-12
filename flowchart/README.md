flowchart TD

A[Raw Crypto Market Data<br/>open, high, low, close,<br/>volume, marketCap, date, crypto_name] 
--> B[Data Preprocessing & Feature Engineering]

B --> B1[True Range (TR)<br/>high − low]
B --> B2[Log Return<br/>ln(close / prev_close)]
B --> B3[Encode Crypto Name<br/>Label Encoding]
B --> B4[Date Features<br/>Day, Month, Year]
B --> B5[ATR(14) Calculation<br/>Target = log(ATR14)]

B1 --> C[Feature Consolidation]
B2 --> C
B3 --> C
B4 --> C
B5 --> C

C --> D[Drop Leakage Columns<br/>atr_14, crypto_name]

D --> E[Final Feature Set<br/>12 Input Features]

E --> F[Train–Test Split]

F --> G[Model Training<br/>XGBoost Regressor<br/>(Tuned Hyperparameters)]

G --> H[Model Evaluation<br/>RMSE • MAE • R²]

H --> I[Model Serialization<br/>xgb_volatility_model.pkl]

I --> J[Flask REST API]

J --> K[POST /api/predict<br/>Accepts 12 Features]

K --> L[Predicted Output<br/>Crypto Volatility<br/>log(ATR14)]

