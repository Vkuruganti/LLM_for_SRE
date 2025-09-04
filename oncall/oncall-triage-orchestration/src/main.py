from ingestion.alert_ingestor import AlertIngestor
from deduplication.deduplicator import Deduplicator
from summarization.summarizer import Summarizer
from clarifying_questions.question_generator import QuestionGenerator
from next_actions.action_proposer import ActionProposer
from servicenow.ticket_drafter import TicketDrafter

def main():
    # Step 1: Ingest alerts
    ingestor = AlertIngestor()
    alerts = ingestor.ingest_alert()

    # Step 2: Deduplicate alerts
    deduplicator = Deduplicator()
    unique_alerts = deduplicator.deduplicate_alerts(alerts)

    # Step 3: Summarize alerts
    summarizer = Summarizer()
    summary = summarizer.summarize_alerts(unique_alerts)

    # Step 4: Generate clarifying questions
    question_generator = QuestionGenerator()
    questions = question_generator.generate_questions(summary)

    # Step 5: Propose next actions
    action_proposer = ActionProposer()
    proposed_actions = action_proposer.propose_actions(unique_alerts, questions)

    # Step 6: Draft ServiceNow ticket
    ticket_drafter = TicketDrafter()
    ticket = ticket_drafter.draft_ticket(proposed_actions, unique_alerts)

    # Output the drafted ticket
    print(ticket)

if __name__ == "__main__":
    main()