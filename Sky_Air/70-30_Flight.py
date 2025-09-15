import pytest
import time
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def test_flight_70(driver):   # better to start with "test_" for pytest
    wait = WebDriverWait(driver, 15)

    #  Open URL
    driver.get("https://uat.skyeairops.tech/operator/cod")
    time.sleep(2)
    print("Opened URL successfully")
    take_screenshot(driver, "open_url")

    #  Login
    driver.find_element(By.ID, "emailId").send_keys("atul.tiwari@skyeair.tech")
    driver.find_element(By.ID, "floatingPassword").send_keys("Atul@123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    print("Logged in successfully")
    take_screenshot(driver, "login_success")

    #  Deliveries
    try:
        delevery = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Deliveries']")))
        delevery.click()
        print("Clicked on Delivery Section")
        take_screenshot(driver, "delivery_section")
    except Exception as e:
        pytest.fail(f"Failed to click Deliveries: {e}")
        time.sleep(3)
    
    # Select AWB Number 
    try:
        awb_number = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-check-input'])[3]")))
        awb_number.click()
        print("Clicked on AWB Number")
        take_screenshot(driver, "awb_number_click")
    except Exception as e:
        pytest.fail(f"Failed to click AWB Number: {e}")

    
#    Bulk Action for Flight 70 30
    try:
        Bulk_Action = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='bulk-btn f-10']")))
        Bulk_Action.click()
        print("Clikc on Bluk Action")
        take_screenshot(driver,"Bulk Action")
    except Exception as e:
        pytest.fail(f"Failes to Click to Bulk Action ")
       
        
# Selct drop Dropdown 