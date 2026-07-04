import pandas as pd

from src.features import build_session_features

logs = pd.DataFrame([
    {
        "timestamp": "2026-06-27 14:30:00",
        "source_ip": "8.8.8.8",
        "event_id": 4624,
        "status": "success",
        "username": "john",
        "is_admin": False,
        "known_device": True,
        "vpn": False,
        "mfa": True,
        "country": "Canada",
        "attack_type": "normal",
    }
])

features = build_session_features(logs)

print(features)
print()
print(features.columns.tolist())