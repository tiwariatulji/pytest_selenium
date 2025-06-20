from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
username.send_keys("rahulkumar@skyeair.tech")
time.sleep(2)

# Password field
password = driver.find_element(By.ID, value="floatingPassword")
password.send_keys("Operator17@prod1996")
time.sleep(2)

# Login 
Login = driver.find_element(By.XPATH, '//button[@type="submit"]')
Login.click()
time.sleep(3)

# COD Flow

New_Del = driver.find_element(By.XPATH, value= "//span[text()='COD']")
New_Del.click()
time.sleep(10)


# Upload Sheet for COD
flipcart_sheet =driver.find_element(By.XPATH, value="//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base']")
flipcart_sheet.click()
time.sleep(2)

# uplaid with excelsheet
upload_file_button = driver.find_element(By.XPATH, value='//button[text()=" Schedule Flight Via Excel "]')
upload_file_button.click()
time.sleep(2)


# # Upload the file
# upload_file = driver.find_element(By.XPATH, value="//input[@type='file']")
# upload_file.send_keys("C:\\Users\\Atul Tiwari\\Downloads\\COD_S")
# # Optional: close the browser

driver.quit()


