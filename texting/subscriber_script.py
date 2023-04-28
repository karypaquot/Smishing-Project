import requests

# this is the End point URL for the API to make the call
url = 'https://api.mobile-text-alerts.com/v3/subscribers/bulk'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 14e5aa70fb86e2ccedf4d289c5e940'
}

# this creates a data set with the subscibers info
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

# Sends a post request to the URL end point with the API to connect
response = requests.post(url, headers=headers, json=data)

print(response.text)
