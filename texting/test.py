<<<<<<< HEAD

from textmagic.rest import TextmagicRestClient
import config
username = "dinguspingusiv"
token = "9Gr5cWltycTl9Zls73HVkCgkbda0uh"
client = TextmagicRestClient(username, token)
message = client.messages.create(phones="+17147470238", text="Hello again!, https://mysecureloginpages.com/")
import requests
import config
amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
print(amnt_of_texts.json())
>>>>>>> 71a6275addf7c15c4f9af9e9075ad30caa1860c5
