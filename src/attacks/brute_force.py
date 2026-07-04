import random
from datetime import timedelta

from company import (
    EXTERNAL_IPS,
    HIGH_RISK_COUNTRIES,
    AUTH_PROTOCOLS,
    EVENT_IDS,
)


def generate(users, devices, start_time, num_attacks=25):
    logs = []

    admin_users = users[users["is_admin"] == True]

    for _ in range(num_attacks):
        attacker_ip = random.choice(EXTERNAL_IPS)
        target_user = admin_users.sample(1).iloc[0]

        attack_start = start_time + timedelta(
        days=random.randint(0, 30),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
)

        attempts = random.randint(20, 60)
        gap_seconds = random.choice([3, 5, 10, 30, 60])

        for i in range(attempts):
            logs.append({
                "timestamp": attack_start + timedelta(seconds=i * gap_seconds),
                "username": target_user["username"],
                "department": target_user["department"],
                "role": target_user["role"],
                "is_admin": target_user["is_admin"],
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
                "attack_type": "brute_force",
            })

        if random.random() < 0.4:
            logs.append({
                "timestamp": attack_start + timedelta(seconds=attempts * gap_seconds + 10),
                "username": target_user["username"],
                "department": target_user["department"],
                "role": target_user["role"],
                "is_admin": target_user["is_admin"],
                "source_ip": attacker_ip,
                "destination_host": "DC01",
                "event_id": EVENT_IDS["LOGIN_SUCCESS"],
                "auth_protocol": random.choice(AUTH_PROTOCOLS),
                "device_id": f"UNKNOWN-{random.randint(100, 999)}",
                "known_device": False,
                "country": random.choice(HIGH_RISK_COUNTRIES),
                "vpn": random.choice([False, True]),
                "mfa": random.choice([False, True]),
                "status": "success",
                "attack_type": "brute_force",
            })

    return logs