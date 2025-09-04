## Repository Folder Overview

### agent
The `agent` folder contains individual AI agent implementations and their dependencies. These agents are designed to perform specific tasks such as alert processing, summarization, and interaction with external APIs. The `requirements.txt` file lists dependencies like Flask (for building REST APIs), PyMuPDF (for PDF processing), and OpenAI (for LLM integration).

### oncall
The `oncall` folder contains the orchestration logic for enterprise on-call triage. It includes modular components for alert ingestion, deduplication, summarization, clarifying question generation, next action proposals, and ServiceNow ticket drafting. This folder also provides deployment scripts, architecture documentation, and integration points for running agents as microservices and leveraging Nvidia Triton for scalable