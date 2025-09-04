class Deduplicator:
    def __init__(self):
        self.seen_alerts = set()

    def deduplicate_alerts(self, alerts):
        unique_alerts = []
        for alert in alerts:
            alert_id = alert.get('id')
            if alert_id not in self.seen_alerts:
                self.seen_alerts.add(alert_id)
                unique_alerts.append(alert)
        return unique_alerts