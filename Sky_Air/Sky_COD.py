from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome options to allow notifications
chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.notifications": 1  # 1 = Allow, 2 = Block
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

try:
    # Open the target URL
    driver.get("https://uat.skyeairops.tech/operator/cod")
    # WebDriverWait(driver, 10).until(EC.title_contains("https://uat.skyeairops.tech/login"))

    # Log in
    driver.find_element(By.ID, "emailId").send_keys("rahulk\umar@skyeair.tech")
    time.sleep(1)

    driver.find_element(By.ID, "floatingPassword").send_keys("Operator17@prod1996")
    time.sleep(1)

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Wait for COD section to load
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='COD']"))).click()
    time.sleep(3)

    # Upload flow
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'schedule-btn')]"))
    ).click()

    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()=" Schedule Flight Via Excel "]'))
    ).click()

    time.sleep(2)

    # # Upload the Excel file
    # upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
    # upload_input.send_keys("C:\\Users\\Atul Tiwari\\Downloads\\COD_Sheet.xlsx")

    # time.sleep(5)  # Optional: wait for upload to complete or next page to load

finally:
    # Close the browser
    driver.quit()
