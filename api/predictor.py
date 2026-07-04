# api/predictor.py

import joblib
import pandas as pd

MODEL_PATH = "models/session_random_forest.pkl"


class ThreatPredictor:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model_path = model_path
        self.model = joblib.load(self.model_path)

    def predict(self, feature_data: dict) -> dict:
        features = pd.DataFrame([feature_data])

        prediction = self.model.predict(features)[0]
        probabilities = self.model.predict_proba(features)[0]
        confidence = probabilities.max()

        return {
            "prediction": str(prediction),
            "confidence": float(confidence),
        }


predictor = ThreatPredictor()