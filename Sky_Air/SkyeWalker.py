from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime, timedelta, date

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

# Select on SkyeWalker Mapping
wait = WebDriverWait(driver, 10)
try:
    Skye_wlaker = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Mapping')]"))
    )
    Skye_wlaker.click()
    print("Clicked on SkyeWalker Section")
    # take_screenshot(driver, "skye_walker_section")
except Exception as e:
    print(f"Error clicking on SkyeWalker section: Skye Walker Not slected  {e}")
raise Exception("Stopping execution due to failure in clicking SkyeWalker section.")

# Attentence Selection 








