import requests
import config
import tkinter as tk
#Function to send the an actual text
def smish(phoneNumber, msg):
    
    resp = requests.post('https://textbelt.com/text', {
    'phone': phoneNumber,
    'message': msg,
    'key': config.api_key,
    })
    print(resp)


def main():
    root = tk.Tk()
    root.geometry('450x200')
    # the label for user_name
    user_name = tk.Label(root, text = "Phone Number").place(x = 40,y = 60) 
    
    # the label for user_password 
    user_password = tk.Label(root, text = "Bait URL").place(x = 50, y = 100) 
    
    submit_button = tk.Button(root,text = "Smish", command = smish).place(x =100, y = 130)
    
    user_name_input_area = tk.Entry(root,width = 30).place(x = 150, y = 60) 
    
    user_password_entry_area = tk.Entry(root, width = 30).place(x = 150,y = 100) 

    var = tk.StringVar(root, "Success")

    messageStatus = tk.Message(root, textvariable=var).place(x= 150, y = 130)

    root.mainloop()

main()


# amnt_of_texts = requests.get('https://textbelt.com/quota/' + config.api_key)
# print(amnt_of_texts.json())

# request for phone number
# phoneNumber = input("Please input a phone number: ")
#request for message
# msg = input("Please your message: ")

# smish(phoneNumber, msg)