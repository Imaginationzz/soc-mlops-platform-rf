import random
from datetime import timedelta

from company import INTERNAL_IPS, SERVERS, AUTH_PROTOCOLS, EVENT_IDS


def generate(users, devices, start_time, num_events=10000):
    logs = []

    device_lookup = {
        row["username"]: row
        for _, row in devices.iterrows()
    }

    for _ in range(num_events):
        user = users.sample(1).iloc[0]
        device = device_lookup[user["username"]]

        success = random.random() < 0.95

        logs.append({
            "timestamp": start_time + timedelta(seconds=random.randint(0, 86400)),
            "username": user["username"],
            "department": user["department"],
            "role": user["role"],
            "is_admin": user["is_admin"],
            "source_ip": random.choice(INTERNAL_IPS),
            "destination_host": random.choice(SERVERS),
            "event_id": EVENT_IDS["LOGIN_SUCCESS"] if success else EVENT_IDS["LOGIN_FAILURE"],
            "auth_protocol": random.choice(AUTH_PROTOCOLS),
            "device_id": device["device_id"],
            "known_device": True,
            "country": user["country"],
            "vpn": random.choice([True, False]),
            "mfa": random.choice([True, True, True, False]),
            "status": "success" if success else "failed",
            "attack_type": "normal",
        })

    return logs