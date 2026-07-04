# api/main.py

from fastapi import FastAPI

from api.schemas import SessionFeatures
from api.predictor import predictor

app = FastAPI(
    title="SOC Threat Detection API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "status": "SOC Threat Detection API is running"
    }


@app.post("/predict")
def predict(features: SessionFeatures):
    return predictor.predict(features.model_dump())