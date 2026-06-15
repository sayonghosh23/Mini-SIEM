def detect_threat(event):

    event = event.lower()

    rules = {
        "failed login": "HIGH",
        "port scan": "HIGH",
        "brute force": "CRITICAL",
        "sql injection": "CRITICAL",
        "xss attack": "MEDIUM"
    }

    for keyword, severity in rules.items():
        if keyword in event:
            return severity

    return "LOW"
