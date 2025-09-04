# filepath: src/utils/triton_client.py
import requests
import json

class TritonClient:
    def __init__(self, triton_url):
        self.triton_url = triton_url

    def infer(self, model_name, input_data):
        url = f"{self.triton_url}/v2/models/{model_name}/infer"
        payload = {
            "inputs": [{"name": "input", "shape": [1], "datatype": "BYTES", "data": [input_data]}]
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["outputs"][0]["data"][0]