def detect_threat(event):

    suspicious = [
        "failed login",
        "port scan",
        "brute force"
    ]

    event = event.lower()

    for keyword in suspicious:
        if keyword in event:
            return "HIGH"

    return "LOW"
