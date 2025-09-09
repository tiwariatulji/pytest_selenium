import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import date, timedelta
import time


@pytest.fixture
def setup_driver():
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


def attach_screenshot(driver, name="screenshot"):
    """Attach screenshot to Allure report"""
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )


@allure.title("Test Schedule Flight")
@allure.description("Verify user can schedule a flight manually with tomorrow’s date and slot selection")
@pytest.mark.usefixtures("setup_driver")
def test_schedule_flight(setup_driver):
    driver = setup_driver

    try:
        #  Open Website
        driver.get("https://uat.skyeairops.tech/operator/cod")
        assert "Operator" in driver.title
        attach_screenshot(driver, "Login Page")

        #  Login
        driver.find_element(By.ID, "emailId").send_keys("atul.tiwari@skyeair.tech")
        driver.find_element(By.ID, "floatingPassword").send_keys("Atul@123")
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        #  Click New Flight
        new_flight = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base'])[1]"))
        )
        new_flight.click()
        attach_screenshot(driver, "After Clicking New Flight")

        #  Click Manual Flight
        manual_flight = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Schedule Flight Manually']"))
        )
        manual_flight.click()

        # Search Tunnel
        search_tunnel = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=\"Search for tunnel by it's name/location\"]"))
        )
        search_tunnel.send_keys("FlipKart")

        #  Select Tunnel
        flipkart_tunnel = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='white-text f-14'][normalize-space()='Flipkart'])[1]"))
        )
        flipkart_tunnel.click()

        #  Click Schedule Delivery
        driver.find_element(By.XPATH, "//button[@class='btn primary-btn f-12 py-2']").click()

        #  Select Tomorrow’s Date
        date_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='exampleFormControlInput1']"))
        )
        date_input.click()
        tomorrow = date.today() + timedelta(days=1)
        formatted_date = f"{tomorrow.day:02d}-{tomorrow.month:02d}-{tomorrow.year}"
        date_input.send_keys(formatted_date)

        # Select Delivery Count
        select_object = Select(driver.find_element(By.XPATH, "//select[@aria-label='Default select example']"))
        select_object.select_by_visible_text("1")

        #  Select Time Slot
        slot_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-dark time-btn br-15 f-12 fw-bold ng-star-inserted'])[2]"))
        )
        slot_select.click()

        #  Final Assertion
        # assert "Schedule" in driver.page_source
        attach_screenshot(driver, "Flight Scheduled Successfully")

        # Slot Selection
        slot_selction = driver.find_element(By.XPATH, value="//button[@class='btn btn-dark slottime-btn br-15 f-12 fw-bold']")
        slot_selction.click()
        print("Clicked on Slot Selection")
   
    except Exception as e:
        attach_screenshot(driver, "Failure Screenshot")
        pytest.fail(f"Test failed due to: Date Slot Picker Is not Clickable  {e}")


