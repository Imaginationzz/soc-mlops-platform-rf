import time
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)

# ------------------------
# Load data
# ------------------------

features = pd.read_csv("data/session_features.csv")

X = features.drop(
    columns=[
        "time_window",
        "source_ip",
        "first_seen",
        "last_seen",
        "label",
    ],
    errors="ignore"
)

y = features["label"]

print("Features:")
print(X.columns.tolist())

print("\nLabels:")
print(y.value_counts())

# ------------------------
# Train/test split
# ------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=None,
)

# ------------------------
# MLflow setup
# ------------------------

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("soc_mlop_platform_rf")

start_time = time.time()

with mlflow.start_run(run_name="session_random_forest_v1"):

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    training_time = time.time() - start_time

    # ------------------------
    # Metrics
    # ------------------------

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted", zero_division=0)
    recall = recall_score(y_test, predictions, average="weighted", zero_division=0)
    f1 = f1_score(y_test, predictions, average="weighted", zero_division=0)

    print("\nAccuracy :", accuracy)
    print("Precision:", precision)
    print("Recall   :", recall)
    print("F1 Score :", f1)

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    report = classification_report(y_test, predictions, zero_division=0)

    print("\nClassification Report:")
    print(report)

    # ------------------------
    # MLflow logging
    # ------------------------

    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_param("class_weight", "balanced")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_param("num_samples", len(features))
    mlflow.log_param("num_features", X.shape[1])
    mlflow.log_param("num_classes", y.nunique())

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision_weighted", precision)
    mlflow.log_metric("recall_weighted", recall)
    mlflow.log_metric("f1_weighted", f1)
    mlflow.log_metric("training_time_seconds", training_time)

    mlflow.log_text("\n".join(X.columns), "feature_names.txt")
    mlflow.log_text(report, "classification_report.txt")

    mlflow.sklearn.log_model(model, "model")

# ------------------------
# Save model locally
# ------------------------

joblib.dump(model, "models/session_random_forest.pkl")

print("\nModel saved to models/session_random_forest.pkl")