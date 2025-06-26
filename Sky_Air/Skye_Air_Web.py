from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
driver.get("https://www.skyeair.tech/")
print("Page Title:", driver.title)
assert "Sky" in driver.title or "Air" in driver.title  # Adjust based on
time.sleep(2)