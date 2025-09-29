import pytest
import logging
import time
from datetime import date, timedelta, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# ---------------- Logging Setup ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("test_log.log", mode="w"),  # log file
        logging.StreamHandler()  # console
    ]
)
logger = logging.getLogger(__name__)

# Utility function to capture screenshot
def take_screenshot(driver, name):
    filename = f"screenshots/{name}.png"
    driver.save_screenshot(filename)
    logger.info(f"Screenshot saved: {filename}")

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
    logger.info("Opened URL successfully")
    take_screenshot(driver, "open_url")

    # Login
    try:
        driver.find_element(By.ID, "emailId").send_keys("admin@skyeair.tech")
        driver.find_element(By.ID, "floatingPassword").send_keys("admin@uat")
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(20)
        logger.info("Logged in successfully")
        take_screenshot(driver, "login_success")
    except Exception as e:
        logger.error(f"Login failed: {e}")
        take_screenshot(driver, "login_failed")
        pytest.fail("Login step failed")

    # Hub and pods selection
    try:
        hub_selected = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/fms-app/hub/pods']")))
        # hub_selected.click()
        logger.info("Hub and Pod is selected")
        take_screenshot(driver, "selected_hub_and_pod")
    except Exception as e:
        logger.error(f"Hub and Pod not selected: {e}")
        take_screenshot(driver, "hub_and_pod_not_selected")
        pytest.fail("Hub and Pod selection failed")
        logger.info()
