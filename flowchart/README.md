```mermaid
flowchart TD
    A[Raw Crypto Market Data] --> B[Feature Engineering]

    B --> B1[True Range = High - Low]
    B --> B2[Log Return = ln(close / prev_close)]
    B --> B3[Label Encode Crypto Name]
    B --> B4[Extract Day Month Year]
    B --> B5[ATR 14 Calculation]

    B1 --> C[Final Dataset]
    B2 --> C
    B3 --> C
    B4 --> C
    B5 --> C

    C --> D[Drop atr_14 and crypto_name]
    D --> E[Final 12 Features]

    E --> F[Train Test Split]
    F --> G[XGBoost Regressor Training]
    G --> H[Model Evaluation RMSE MAE R2]

    H --> I[Save Model xgb_volatility_model.pkl]
    I --> J[Flask API]
    J --> K[POST /api/predict]
    K --> L[Predict log ATR14]
```
