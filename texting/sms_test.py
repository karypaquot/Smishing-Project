import requests

# Set up API credentials
url = 'https://api.mobile-text-alerts.com/v3/'
api_key = '14e5aa70fb86e2ccedf4d289c5e940'
headers = {'Authorization': f'Bearer {api_key}'}

# Define function to send a message to all subscribers
def send_message(message):
    data = {
        "allSubscribers": True,
        "message": message
    }
    response = requests.post(url + 'send', headers=headers, json=data)
    print(response.text)
    return response.json()

# Send message to all subscribers
send_message('Hello Julia this is a test. https://mysecureloginpages.com')