import requests
import config
from tkinter import *
from tkinter import ttk


# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

#Send the an actual text
# resp = requests.post('https://textbelt.com/text', {
#   'phone': '17142735406',
#   'message': 'You gae',
#   'key': '41c11a171f8328bdb577d003f390cdae33f37bceRW0VEUeOQDFeoq0bsIuitq7NT',
# })
# print(resp.json())

amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
print(amnt_of_texts.json())