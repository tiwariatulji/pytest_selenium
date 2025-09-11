import pytest
import os
from datetime import datetime, timedelta, date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def take_screenshot(driver, name):
    """Take a screenshot and save it with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    filename = f"{screenshot_dir}/{name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename


def test_flight_booking_flow(browser):
    driver = browser
    wait = WebDriverWait(driver, 10)

    try:
        # Open the target URL
        driver.get("https://uat.skyeairops.tech/operator/cod")

        # Assert page title
        assert "Operator Interface" in driver.title, f"Expected 'Operator Interface' in title, got {driver.title}"

        # Login
        username = wait.until(EC.presence_of_element_located((By.ID, "emailId")))
        username.send_keys("atul.tiwari@skyeair.tech")

        password = wait.until(EC.presence_of_element_located((By.ID, "floatingPassword")))
        password.send_keys("Atul@123")

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        login_button.click()

        # Flight Roster Flow - New Flight
        new_flight = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base'])[1]"))
        )
        new_flight.click()

        # Manual Flight
        manual_flight = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Schedule Flight Manually']"))
        )
        manual_flight.click()

        # Search Tunnel
        search_tunnel = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=\"Search for tunnel by it's name/location\"]"))
        )
        search_tunnel.send_keys("FlipKart")

        # Select Flipkart Tunnel
        flipkart_tunnel = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='white-text f-14'][normalize-space()='Flipkart'])[1]"))
        )
        flipkart_tunnel.click()

        # Schedule Delivery
        schedule_delivery = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn primary-btn f-12 py-2']")))
        schedule_delivery.click()

        # Select Date
        date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='exampleFormControlInput1']")))
        date_input.click()
        tomorrow = date.today() + timedelta(days=1)
        formatted_date = f"{tomorrow.day:02d}-{tomorrow.month:02d}-{tomorrow.year}"
        date_input.send_keys(formatted_date)

        # Select Delivery Count
        delivery_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@aria-label='Default select example']")))
        select_object = Select(delivery_select)
        select_object.select_by_visible_text("1")

        # Select Slot
        slot_select = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-dark time-btn br-15 f-12 fw-bold ng-star-inserted'])[2]")))
        slot_select.click()

        # Slot Selection Button
        slot_selection = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-dark slottime-btn br-15 f-12 fw-bold']")))
        slot_selection.click()

        # Time Slot Input
        time_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='time' and @formcontrolname='timeSlot']")))
        selected_time = "22:00"
        time_input.send_keys(selected_time)

        # Select Time Slot Button
        select_time_slot = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-dark time-btn br-15 f-12 fw-bold ng-star-inserted'])[1]")))
        select_time_slot.click()

        # Next Button
        next_button_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn primary-btn f-12 py-2']")))
        next_button_1.click()

        # Client Organization
        organization = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@class, 'form-select')]")))
        select_object = Select(organization)
        select_object.select_by_visible_text("ECOM")

        # Client Name
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 2)
        selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
        client_name = selects[1]
        select_object = Select(client_name)
        wait.until(lambda driver: len(select_object.options) > 1)
        select_object.select_by_visible_text("Abhinav Dhiman")

        # TakeOff Pilot
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 3)
        selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
        takeoff_pilot = selects[2]
        select_object = Select(takeoff_pilot)
        wait.until(lambda driver: len(select_object.options) > 1)
        select_object.select_by_visible_text("Animesh Verma")

        # Landing Pilot
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 4)
        selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
        landing_pilot = selects[3]
        select_object = Select(landing_pilot)
        wait.until(lambda driver: len(select_object.options) > 2)
        select_object.select_by_visible_text("Tarun Sadhya")

        # Drone Selection
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 5)
        selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
        drone = selects[4]
        select_object = Select(drone)
        wait.until(lambda driver: len(select_object.options) > 2)
        select_object.select_by_visible_text("Hexo One")

        # Next Button after Client Details
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn primary-btn f-12 py-2']")))
        next_button.click()

        # Select Time Slot After Client Details
        time_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='time-active btn btn-dark']")))
        time_select.click()

        # Checkbox
        check_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'checkbox-position')]")))
        check_box.click()

        # Proceed to Overview
        proceed_overview = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn primary-btn')]")))
        proceed_overview.click()

        # Final Submit
        final_submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Confirm my order ']")))
        final_submit.click()

        # Done for Now
        done_for_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-dark-border btn-hover btn-block f-12 py-2']")))
        done_for_now.click()

        # Return to Flight Roster
        return_flight_roster = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Flight Roster']")))
        return_flight_roster.click()

        # Approve Flight
        approve_flight = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator approve-btn mat-button mat-button-base'])[1]")))
        approve_flight.click()

        # Take success screenshot
        take_screenshot(driver, "flight_booking_success")

    except Exception as e:
        # Take failure screenshot
        screenshot_path = take_screenshot(driver, "flight_booking_failure")
        pytest.fail(f"Test failed: {str(e)}. Screenshot saved at {screenshot_path}")

