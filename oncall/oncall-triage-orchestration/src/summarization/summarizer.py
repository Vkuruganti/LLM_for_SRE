class Summarizer:
    def summarize_alerts(self, alerts):
        """
        Generate a concise summary of the alerts for easier understanding.
        
        Parameters:
        alerts (list): A list of alert dictionaries to summarize.

        Returns:
        str: A summary of the alerts.
        """
        if not alerts:
            return "No alerts to summarize."

        summary = []
        for alert in alerts:
            summary.append(f"Alert ID: {alert['id']}, Severity: {alert['severity']}, Message: {alert['message']}")

        return "\n".join(summary)