import requests

url = 'https://api.mobile-text-alerts.com/v3/subscribers/bulk'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 14e5aa70fb86e2ccedf4d289c5e940'
}

data = [
    {
        "firstName": "Karina",
        "lastName": "Hernandez",
        "number": 15627398942,
        "email": "",
        "groupIds": [175380],
        "subscriberFieldIds": {
        }
    }
]

response = requests.post(url, headers=headers, json=data)

print(response.text)
