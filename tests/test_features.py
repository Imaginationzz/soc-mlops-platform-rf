import pandas as pd
import pytest

from src.features import build_session_features


@pytest.fixture
def sample_logs():
    return pd.DataFrame([
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
        },
        {
            "timestamp": "2026-06-27 14:31:00",
            "source_ip": "8.8.8.8",
            "event_id": 4624,
            "status": "failed",
            "username": "john",
            "is_admin": False,
            "known_device": True,
            "vpn": False,
            "mfa": True,
            "country": "Canada",
            "attack_type": "normal",
        },
        {
            "timestamp": "2026-06-27 14:32:00",
            "source_ip": "8.8.8.8",
            "event_id": 4624,
            "status": "success",
            "username": "alice",
            "is_admin": False,
            "known_device": False,
            "vpn": False,
            "mfa": False,
            "country": "Canada",
            "attack_type": "normal",
        },
    ])


def test_build_session_features_returns_dataframe(sample_logs):
    features = build_session_features(sample_logs)

    assert isinstance(features, pd.DataFrame)


def test_build_session_features_has_expected_columns(sample_logs):
    features = build_session_features(sample_logs)

    expected_columns = [
        "time_window",
        "source_ip",
        "total_logins",
        "failed_logins",
        "successful_logins",
        "unique_users",
        "admin_targets",
        "unknown_devices",
        "vpn_usage",
        "mfa_usage",
        "unique_countries",
        "label",
        "failure_rate",
        "success_rate",
        "unknown_device_rate",
        "mfa_rate",
    ]

    assert list(features.columns) == expected_columns


def test_total_logins(sample_logs):
    features = build_session_features(sample_logs)

    assert features.loc[0, "total_logins"] == 3