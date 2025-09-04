def log_message(message: str) -> None:
    print(f"[LOG] {message}")

def format_alert_data(alert_data: dict) -> str:
    return f"Alert: {alert_data.get('title', 'No Title')} - Severity: {alert_data.get('severity', 'Unknown')}"

def validate_alert_data(alert_data: dict) -> bool:
    required_fields = ['title', 'severity', 'timestamp']
    return all(field in alert_data for field in required_fields)