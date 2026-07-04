"""
Company-wide constants for the SOC MLOps platform.
"""

COMPANY_NAME = "Contoso Security"

DEPARTMENTS = [
    "IT",
    "HR",
    "Finance",
    "Sales",
    "Marketing",
    "Operations",
]

COUNTRIES = [
    "Canada",
    "USA",
    "UK",
]

HIGH_RISK_COUNTRIES = [
    "Russia",
    "China",
    "North Korea",
    "Brazil",
]

INTERNAL_IPS = [
    "10.0.0.5",
    "10.0.0.10",
    "10.0.0.15",
    "192.168.1.20",
    "172.16.0.8",
]

EXTERNAL_IPS = [
    "203.0.113.50",
    "198.51.100.25",
    "45.33.22.10",
    "91.200.14.8",
]

SERVERS = [
    "DC01",
    "DC02",
    "VPN01",
    "FILE01",
    "WEB01",
    "SQL01",
    "MAIL01",
]

AUTH_PROTOCOLS = [
    "Kerberos",
    "NTLM",
]

EVENT_IDS = {
    "LOGIN_SUCCESS": 4624,
    "LOGIN_FAILURE": 4625,
    "LOGOFF": 4634,
    "EXPLICIT_CREDENTIALS": 4648,
    "SPECIAL_PRIVILEGES": 4672,
    "USER_CREATED": 4720,
    "GROUP_MEMBER_ADDED": 4728,
}

DEVICE_TYPES = [
    "Laptop",
    "Desktop",
    "Workstation",
    "Server",
]

OPERATING_SYSTEMS = [
    "Windows 11",
    "Windows 10",
    "Ubuntu 24.04",
]