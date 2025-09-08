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
username.send_keys("atul.tiwari@skyeair.tech")
time.sleep(2)

# Password field
password = driver.find_element(By.ID, value="floatingPassword")
password.send_keys("Atul@123")
time.sleep(2)

# Login 
Login = driver.find_element(By.XPATH, '//button[@type="submit"]')
Login.click()
time.sleep(10)

# Flight Roster Flow

# Wait for the button to be clickable before clicking
try:
    New_Flight = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base'])[1]"))
    )
    New_Flight.click()
    print("Clicked on Manual Flight Selection")
    time.sleep(10)
except Exception as e:
    print(f"Error finding or clicking the flight button: {e}")
    print("Page source around the error:")
    # print(driver.page_source[:2000])  # Print first 2000 chars of page source for debugging

manual_flight = driver.find_element(By.XPATH, value="//span[text()='Manual Flight']")
manual_flight.click()

