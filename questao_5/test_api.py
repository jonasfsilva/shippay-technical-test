import requests

url = "http://127.0.0.1:5000/users"

payload = {
    "nome": "Jonas",
    "email": "jonas@example.com",
    "role_id": 1,
    "claim_ids": [1, 2],
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print("Status code:", response.status_code)
print("Response:", response.text)
