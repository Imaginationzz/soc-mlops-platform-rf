import random
from datetime import timedelta

from company import (
    EXTERNAL_IPS,
    HIGH_RISK_COUNTRIES,
    AUTH_PROTOCOLS,
    EVENT_IDS,
)


def generate(users, devices, start_time, num_attacks=300):
    logs = []

    for _ in range(num_attacks):
        attacker_ip = random.choice(EXTERNAL_IPS)

        attack_start = start_time + timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59),
        )

        # Password spraying = one/few attempts across many users
        target_users = users.sample(
            n=random.randint(15, 40),
            replace=False
        )

        for _, user in target_users.iterrows():
            logs.append({
                "timestamp": attack_start + timedelta(
                    seconds=random.randint(0, 240)
                ),
                "username": user["username"],
                "department": user["department"],
                "role": user["role"],
                "is_admin": user["is_admin"],
                "source_ip": attacker_ip,
                "destination_host": "DC01",
                "event_id": EVENT_IDS["LOGIN_FAILURE"],
                "auth_protocol": random.choice(AUTH_PROTOCOLS),
                "device_id": f"UNKNOWN-{random.randint(100, 999)}",
                "known_device": False,
                "country": random.choice(HIGH_RISK_COUNTRIES),
                "vpn": random.choice([False, False, True]),
                "mfa": False,
                "status": "failed",
                "attack_type": "password_spraying",
            })

    return logs