class AlertIngestor:
    def __init__(self):
        self.alerts = []

    def ingest_alert(self, alert):
        self.alerts.append(alert)
        return self.alerts