# api/schemas.py

from pydantic import BaseModel


class SessionFeatures(BaseModel):
    total_logins: int
    failed_logins: int
    successful_logins: int
    unique_users: int
    admin_targets: int
    unknown_devices: int
    vpn_usage: int
    mfa_usage: int
    unique_countries: int
    failure_rate: float
    success_rate: float
    unknown_device_rate: float
    mfa_rate: float