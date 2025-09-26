import pytest
import time
from datetime import date, timedelta, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# Utility function to capture screenshot
def take_screenshot(driver, name):
    filename = f"screenshots/{name}.png"
    driver.save_screenshot(filename)
    print(f" Screenshot saved: {filename}")

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_user(driver):
    wait = WebDriverWait(driver, 15)

    # Open URL
    driver.get("https://d38eiqln1spwnm.cloudfront.net/login")
    time.sleep(2)
    print("Opened URL successfully")
    take_screenshot(driver, "open_url")

    # Login
    driver.find_element(By.ID, "emailId").send_keys("admin@skyeair.tech")
    driver.find_element(By.ID, "floatingPassword").send_keys("admin@uat")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(20)
    print("Logged in successfully")
    take_screenshot(driver, "login_success")
    
    # hub and pods selection

    try:
        hub_selected = wait(EC.element_to_be_clickable((By.XPATH,"//a[@href='/fms-app/hub/pods']")))
        hub_selected.click()
        print("Hub and Pod is selected ")
        take_screenshot(driver,"Slected hub and pod")
    except Exception as e:
        pytest.fail(f'Hub and Pod not selected')
        take_screenshot(driver,"Hub and Pod not selected")
    