import requests
import config
import tkinter as tk

root = tk.Tk()
#dimensions of window
root.geometry("800x500")
#title of window
root.title("Smshysmsh")

label = tk.Label(root, text='Smshy', font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox =  tk.Text(root, height=3, font=('Arial', 15))
textbox.pack(padx=50);

root.mainloop()

#Send the an actual text
def smish():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '17142735406',
    'message': 'You gae',
    'key': '41c11a171f8328bdb577d003f390cdae33f37bceRW0VEUeOQDFeoq0bsIuitq7NT',
    })
    print(resp.json())

amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
print(amnt_of_texts.json())