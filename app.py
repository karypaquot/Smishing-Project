from flask import Flask, render_template, request
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    driver.maximize_window()

    input_email = driver.find_element(By.ID, 'email')
    input_pass = driver.find_element(By.ID, 'pass')

    input_email.clear()
    input_email.send_keys(email)
    time.sleep(2)
    input_pass.clear()
    input_pass.send_keys(password)

    input_pass.submit()
    
    
    return 'Form submitted and processed!'

if __name__ == '__main__':
    app.run(debug=True)