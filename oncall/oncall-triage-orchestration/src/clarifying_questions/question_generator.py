class QuestionGenerator:
    def generate_questions(self, summarized_alert):
        questions = []
        
        if 'host' in summarized_alert:
            questions.append(f"Is the affected host {summarized_alert['host']} isolated?")
        
        if 'token' in summarized_alert:
            questions.append("Has the token been revoked?")
        
        if 'severity' in summarized_alert:
            questions.append(f"What is the severity level of the alert: {summarized_alert['severity']}?")
        
        if 'timestamp' in summarized_alert:
            questions.append(f"When did the alert occur? Timestamp: {summarized_alert['timestamp']}")
        
        return questions