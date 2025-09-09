from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime, timedelta

# Chrome Options for Allowing Notification
chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.notifications": 1  # 1 = Allow, 2 = Block
}
chrome_options.add_experimental_option("prefs", prefs)

# Launch Chrome with options
driver = webdriver.Chrome(options=chrome_options) 
driver.maximize_window()

# Open the target URL
driver.get("https://uat.skyeairops.tech/operator/cod")
time.sleep(2)

# Print the page title
print(driver.title)

username = driver.find_element(By.ID, value="emailId")
username.send_keys("atul.tiwari@skyeair.tech")
time.sleep(2)

# Password field
password = driver.find_element(By.ID, value="floatingPassword")
password.send_keys("Atul@123")
time.sleep(2)

# Login 
Login = driver.find_element(By.XPATH, '//button[@type="submit"]')
Login.click()
time.sleep(3)

# COD Flow

New_Del = driver.find_element(By.XPATH, value= "//span[text()='COD']")
New_Del.click()
print("Clicked on COD")
time.sleep(10)

# Select dropdown value
how_many = driver.find_element(By.XPATH, value="//select[@aria-label='Default select example']")
how_many.send_keys("1")
how_many.click()
print("Selected 1 Delivery")
time.sleep(5)

hub_select = driver.find_element(By.XPATH, value="//select[@class='form-select']")
hub_select.click()
time.sleep(2)


# Upload Sheet for COD
# flipcart_sheet =driver.find_element(By.XPATH, value="//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base']")
# flipcart_sheet.click()

# time.sleep(2)

# # upl with excelsheet
# upload_file_button = driver.find_element(By.XPATH, value='//button[text()=" Schedule Flight Via Excel "]')
# upload_file_button.click()
# time.sleep(2)

# # select hub name
# select_dropdown = driver.find_element(By.XPATH, value="//option[text()=' Flipkart -- Flipkart-00001 ']")

# driver.execute_script("window.scrollBy({ top: 0, left: 300, behavior: 'smooth' });")

# Edit_Hub = driver.find_element(By.XPATH, value="//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']")
# Edit_Hub.click()

driver.quit()


