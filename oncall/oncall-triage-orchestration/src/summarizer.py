# filepath: src/summarization/summarizer.py
from utils.triton_client import TritonClient

class Summarizer:
    def __init__(self, triton_url):
        self.triton_client = TritonClient(triton_url)

    def summarize(self, alert_text):
        return self.triton_client.infer("summarization-model", alert_text)