class TicketDrafter:
    def __init__(self, service_now_client):
        self.service_now_client = service_now_client

    def draft_ticket(self, alert_summary, proposed_actions, additional_info):
        ticket_data = {
            "short_description": f"Alert: {alert_summary}",
            "description": f"Summary of the alert: {alert_summary}\nProposed Actions: {', '.join(proposed_actions)}\nAdditional Info: {additional_info}",
            "priority": self.determine_priority(alert_summary),
            "category": "Incident",
            "subcategory": "Security"
        }
        response = self.service_now_client.create_ticket(ticket_data)
        return response

    def determine_priority(self, alert_summary):
        # Logic to determine priority based on alert summary
        if "critical" in alert_summary.lower():
            return "1 - Critical"
        elif "high" in alert_summary.lower():
            return "2 - High"
        else:
            return "3 - Medium"