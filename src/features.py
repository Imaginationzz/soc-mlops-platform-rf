import pandas as pd


def build_session_features(logs: pd.DataFrame, window_minutes: int = 5) -> pd.DataFrame:
    logs = logs.copy()
    logs["timestamp"] = pd.to_datetime(logs["timestamp"])

    logs["time_window"] = logs["timestamp"].dt.floor(f"{window_minutes}min")

    features = (
        logs.groupby(["time_window", "source_ip"])
        .agg(
            total_logins=("event_id", "count"),
            failed_logins=("status", lambda x: (x == "failed").sum()),
            successful_logins=("status", lambda x: (x == "success").sum()),
            unique_users=("username", "nunique"),
            admin_targets=("is_admin", lambda x: (x == True).sum()),
            unknown_devices=("known_device", lambda x: (x == False).sum()),
            vpn_usage=("vpn", lambda x: (x == True).sum()),
            mfa_usage=("mfa", lambda x: (x == True).sum()),
            unique_countries=("country", "nunique"),
            label=("attack_type", lambda x: x[x != "normal"].iloc[0] if (x != "normal").any() else "normal"),
        )
        .reset_index()
    )

    features["failure_rate"] = features["failed_logins"] / features["total_logins"]
    features["success_rate"] = features["successful_logins"] / features["total_logins"]
    features["unknown_device_rate"] = features["unknown_devices"] / features["total_logins"]
    features["mfa_rate"] = features["mfa_usage"] / features["total_logins"]

    return features


if __name__ == "__main__":
    logs = pd.read_csv("data/auth_logs.csv")

    features = build_session_features(logs)

    features.to_csv("data/session_features.csv", index=False)

    print("Saved data/session_features.csv")
    print(features.head())
    print(features["label"].value_counts())