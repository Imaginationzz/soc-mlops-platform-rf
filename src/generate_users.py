import random
import pandas as pd

from company import DEPARTMENTS, COUNTRIES


def generate_users():

    random.seed(42)

    users = []

    for i in range(1, 51):
        users.append({
            "username": f"user{i:03}",
            "department": random.choice(DEPARTMENTS),
            "country": random.choice(COUNTRIES),
            "role": "Employee",
            "is_admin": False,
        })

    admin_indexes = random.sample(range(50), 3)

    for idx in admin_indexes:
        users[idx]["role"] = "Administrator"
        users[idx]["is_admin"] = True

    return pd.DataFrame(users)


if __name__ == "__main__":

    df = generate_users()

    df.to_csv("data/users.csv", index=False)

    print("Generated data/users.csv")
    print(df.head())
    print(df["role"].value_counts())