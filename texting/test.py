
from textmagic.rest import TextmagicRestClient
import config
username = "dinguspingusiv"
token = "9Gr5cWltycTl9Zls73HVkCgkbda0uh"
client = TextmagicRestClient(username, token)
message = client.messages.create(phones="+17147470238", text="Hello again!, https://mysecureloginpages.com/")