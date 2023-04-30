import requests
import config
from twilio.rest import Client


account_sid = 'AC93a9fb26b5c61143fe8814d36f24fb87'
auth_token = config.twilio_auth
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18444340329',
  body = "https://www.yahoo.com/",
  to='+17147470238'
)
print(message.sid)
# amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
# print(amnt_of_texts.json())