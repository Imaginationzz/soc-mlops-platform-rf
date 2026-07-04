from datetime import datetime

import pandas as pd

from generate_users import generate_users
from generate_devices import generate_devices

from attacks.normal import generate as generate_normal
from attacks.brute_force import generate as generate_bruteforce
from attacks.password_spraying import generate as generate_password_spraying


def main():
    users = generate_users()
    devices = generate_devices(users)

    start_time = datetime(2026, 1, 1)

    logs = []

    logs.extend(
        generate_normal(
            users=users,
            devices=devices,
            start_time=start_time,
            num_events=10000,
        )
    )

    logs.extend(
        generate_bruteforce(
            users=users,
            devices=devices,
            start_time=start_time,
            num_attacks=500,
        )
    )
    logs.extend(
        generate_password_spraying(
            users=users,
            devices=devices,
            start_time=start_time,
            num_attacks=300,
        )
)

    df = pd.DataFrame(logs)

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    df.to_csv("data/auth_logs.csv", index=False)

    print("Generated data/auth_logs.csv")
    print(df.head())
    print(df["attack_type"].value_counts())


if __name__ == "__main__":
    main()