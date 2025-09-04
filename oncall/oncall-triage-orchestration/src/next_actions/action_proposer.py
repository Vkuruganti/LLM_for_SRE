class ActionProposer:
    def propose_actions(self, alerts, questions):
        actions = []
        
        for alert in alerts:
            if "host" in alert:
                actions.append(f"Isolate host: {alert['host']}")
            if "token" in alert:
                actions.append(f"Revoke token: {alert['token']}")
        
        if not actions:
            actions.append("No immediate actions required.")
        
        return actions