from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome Options to allow notifications
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 1}
chrome_options.add_experimental_option("prefs", prefs)

# Launch Chrome
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    # Open the target URL
    driver.get("https://uat.skyeairops.tech/operator/cod")
    time.sleep(2)

    # Verify page title
    print("Page Title:", driver.title)
    assert "Sky" in driver.title or "COD" in driver.title  # Adjust based on actual title
    print("✅ Page loaded successfully.")

    # Login
    driver.find_element(By.ID, "emailId").send_keys("rahulkumar@skyeair.tech")
    driver.find_element(By.ID, "floatingPassword").send_keys("Operator17@prod1996")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    print("✅ Login submitted.")

    # Click on COD
    New_Del = driver.find_element(By.XPATH, "//span[text()='COD']")
    New_Del.click()
    time.sleep(5)
    print("✅ COD section opened.")

    # Click on "Upload Sheet"
    flipcart_sheet = driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base']")
    flipcart_sheet.click()
    time.sleep(2)
    print("✅ Upload sheet button clicked.")

    # Click on "Schedule Flight Via Excel"
    upload_file_button = driver.find_element(By.XPATH, '//button[text()=" Schedule Flight Via Excel "]')
    upload_file_button.click()
    time.sleep(2)
    print("✅ Schedule via Excel clicked.")

    print("🎉 Test Passed!")

except AssertionError as e:
    print("❌ Assertion Failed:", e)
except Exception as e:
    print("❌ Test Failed:", e)
finally:
    driver.quit()
# Ensure the browser is closed after the test
    print("Browser closed.")