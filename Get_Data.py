import requests
import json

LN_BITS_URL = "YOUR_LIGHTNING_NODE_URL"
API_KEY = "YOUR_INVOICE_READ_KEY"

headers = {
    "X-Api-Key": API_KEY
}

response = requests.get(
    f"{LN_BITS_URL}/boltcards/api/v1/cards",
    headers=headers,
    timeout=10
)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print("Error:", response.status_code, response.text)
