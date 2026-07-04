import random
import pandas as pd

from company import DEVICE_TYPES, OPERATING_SYSTEMS


def generate_devices(users: pd.DataFrame) -> pd.DataFrame:
    random.seed(42)

    devices = []

    for i, row in users.iterrows():
        devices.append({
            "username": row["username"],
            "device_id": f"DEVICE-{i+1:03}",
            "device_type": random.choice(DEVICE_TYPES),
            "operating_system": random.choice(OPERATING_SYSTEMS),
            "known_device": True,
        })

    return pd.DataFrame(devices)


if __name__ == "__main__":

    users = pd.read_csv("data/users.csv")

    devices_df = generate_devices(users)

    devices_df.to_csv("data/devices.csv", index=False)

    print("Generated data/devices.csv")
    print(devices_df.head())