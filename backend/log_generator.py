import requests

events = [
    "Failed Login Attempt",
    "Port Scan Detected",
    "SQL Injection Attempt",
    "Normal User Login",
    "Brute Force Attack",
    "XSS Attack Detected"
]

for event in events:

    response = requests.post(
        "http://127.0.0.1:8000/log",
        params={
            "source": "simulator",
            "event": event
        }
    )

    print(response.json())
