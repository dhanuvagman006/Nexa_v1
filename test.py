
import requests

BASE_URL = "https://api.openrouter.ai/v1"
PROVISIONING_API_KEY = "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"
response = requests.post(
    f"{BASE_URL}/",
    headers={
        "Authorization": f"Bearer {PROVISIONING_API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "name": "Customer Instance Key",
        "label": "customer-123",
    }
)