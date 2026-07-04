import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

users = ["admin", "yazid", "alice", "bob", "sarah", "john"]
ips = ["192.168.1.10", "192.168.1.20", "10.0.0.5", "172.16.0.8"]

logs = []
start_time = datetime(2026, 6, 28, 10, 0, 0)

# Normal login behavior
for i in range(200):
    logs.append({
        "timestamp": start_time + timedelta(seconds=i * 60),
        "user": random.choice(users),
        "source_ip": random.choice(ips),
        "event_type": "login",
        "status": random.choice(["success", "success", "success", "failed"]),
        "label": "normal"
    })

# Brute force attack
attack_ip = "203.0.113.50"
for i in range(40):
    logs.append({
        "timestamp": start_time + timedelta(seconds=13000 + i * 5),
        "user": "admin",
        "source_ip": attack_ip,
        "event_type": "login",
        "status": "failed",
        "label": "brute_force"
    })

# Success after brute force
logs.append({
    "timestamp": start_time + timedelta(seconds=13210),
    "user": "admin",
    "source_ip": attack_ip,
    "event_type": "login",
    "status": "success",
    "label": "brute_force"
})


df = pd.DataFrame(logs)
df = df.sort_values("timestamp")

df.to_csv("data/auth_logs.csv", index=False)

print("Generated data/auth_logs.csv")
print(df.head())
print(df["label"].value_counts())