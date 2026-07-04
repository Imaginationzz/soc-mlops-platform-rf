# SOC MLOps Platform

## Overview

An end-to-end MLOps pipeline for detecting authentication attacks.

Features:

- Synthetic log generation
- Feature engineering
- Random Forest classifier
- MLflow experiment tracking
- FastAPI inference API
- Docker containerization
- AWS EC2 deployment

## Tech Stack

- Python
- Pandas
- Scikit-Learn
- FastAPI
- MLflow
- Docker
- AWS EC2
- GitHub Actions (coming soon)

## Project Structure

src/
api/
models/
tests/
data/

## Run

python src/train.py

Start API

uvicorn api.main:app --reload

Docker

docker build -t soc-mlops-platform .
docker run -p 8000:8000 soc-mlops-platform
