import csv
import requests

# Set up API credentials
url = 'https://api.mobile-text-alerts.com/v3/'
api_key = '14e5aa70fb86e2ccedf4d289c5e940'
headers = {'Authorization': f'Bearer {api_key}'}

# Define function to create subscribers
def create_subscriber(subscriber):
    data = [{
        "firstName": subscriber['first_name'],
        "lastName": subscriber['last_name'],
        "number": subscriber['phone_number'],
        #"email": subscriber['email'],
        "groupIds": [175380] # this is the group ID for 'Campaign'
        #"subscriberFieldIds": {}
    }]
    response = requests.post(url + 'subscribers/bulk', headers=headers, json=data)
    return response.json()

# Define function to send a message to all subscribers
# Endpoint URL is limited to 15 requests per 15 seconds
def send_message(message):
    data = {
        "allSubscribers": True,
        "message": message
    }
    response = requests.post(url + 'send', headers=headers, json=data)
    return response.json()

# Read data from CSV file and create subscribers
with open('subscribers.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        create_subscriber(row)

# Send message to all subscribers
send_message('Hello Julia this is a test. https://mysecureloginpages.com')
