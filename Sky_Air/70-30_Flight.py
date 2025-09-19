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

def test_flight_70(driver):
    wait = WebDriverWait(driver, 15)

    # Open URL
    driver.get("https://uat.skyeairops.tech/operator/cod")
    time.sleep(2)
    print("Opened URL successfully")
    take_screenshot(driver, "open_url")

    # Login
    driver.find_element(By.ID, "emailId").send_keys("atul.tiwari@skyeair.tech")
    driver.find_element(By.ID, "floatingPassword").send_keys("Atul@123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    print("Logged in successfully")
    take_screenshot(driver, "login_success")

    # Deliveries
    try:
        delivery = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Deliveries']")))
        delivery.click()
        print("Clicked on Delivery Section")
        take_screenshot(driver, "delivery_section")
    except Exception as e:
        pytest.fail(f"Failed to select pilot: {e}")
        pytest.fail(f"Failed to click Deliveries: {e}")

    # Select AWB Number 
    try:
        awb_number = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-check-input'])[3]")))
        awb_number.click()
        print("Clicked on AWB Number")
        take_screenshot(driver, "awb_number_click")
    except Exception as e:
        pytest.fail(f"Failed to click AWB Number: {e}")

    # Bulk Action
    try:
        bulk_action = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='bulk-btn f-10']")))
        bulk_action.click()
        print("Clicked on Bulk Action")
        take_screenshot(driver, "bulk_action")
    except Exception as e:
        pytest.fail(f"Failed to click Bulk Action: {e}")

    # Click on the dropdown

    # dropdowns = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "mat-select-arrow")]')))
    # dropdowns[2].click()
    # print("Clicked on dropdown")
    # time.sleep(2)
    # dropdowns = wait.until(
    # EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "mat-select-arrow")]')))
    # dropdowns[2].click()
    # print("Clicked on dropdown")


    # Click dropdown
    dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//div[contains(@class,"mat-select-arrow")])[4]'))
    )
    dropdown.click()
    time.sleep(5)

# Now click option and Select "Schedule Flight"
    schedule_flight = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[@class="mat-option-text"][contains(., "Schedule Flight")]')))
    schedule_flight.click()
    print("Selected Schedule Flight")

    try:
       button_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Submit']")))
       button_click.click()
       print("Buuton is click for 70 30 Flight ")
       take_screenshot(driver,"Button Click")

    except Exception as e:
         pytest.fail("Button is not clickable")

    # // Select A tunnel
    try:
        select_tunnel = wait.until(EC.element_to_be_clickable((By.XPATH,"(//span[@class='mat-radio-outer-circle'])[1]")))
        select_tunnel.click()
        print("Select skye tunnel")
        take_screenshot(driver,"Select skye Tunnel")
    except Exception as e:
         pytest.fail("Tunnel not slected Pls select tunne first ")
       
    #  Next Button and Time select 
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-primary f-12']")))
    next_button.click()
    print("Next button clik")
    time.sleep(5)
    
    # select time slot
    try:
        # Select time
        select_start_time = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='startTime']")))
        select_end_time   = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='endTime']")))

        # Current time
        current_time = datetime.now().strftime("%H:%M")
        # End time = current time + 5 minutes
        end_time = (datetime.now() + timedelta(minutes=5)).strftime("%H:%M")

        # Use JavaScript to set values to avoid automatic clearing
        driver.execute_script("arguments[0].value = arguments[1];", select_start_time, current_time)
        driver.execute_script("arguments[0].value = arguments[1];", select_end_time, end_time)

        # Trigger change event if necessary
        driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", select_start_time)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change', { bubbles: true }));", select_end_time)

        print(f"All start time {current_time}")
        print(f"End time {end_time}")
        take_screenshot(driver,"Time select")
        time.sleep(5)
    except Exception as e:
        pytest.fail(f"Failed during select and start and end time {e}")
        

    # select Take off pilot
    try:
        pilot_dropdown = wait.until(EC.presence_of_element_located((By.ID, "takeOffPilot")))
        
        # Use Select class to choose pilot
        select = Select(pilot_dropdown)
        select.select_by_visible_text("Animesh Verma")
        print(" Pilot 'Animesh Verma' selected successfully")
        time.sleep(1)
    except Exception as e:
        pytest.fail(f"Animesh Verma is not selected")


#  Landing Pilot Name 
   
    try:
        landing_pilot_dropdown = wait.until(EC.presence_of_element_located((By.ID, "landingPilot")))
        select = Select(landing_pilot_dropdown)
        select.select_by_visible_text("Atul tiwari")
        landing_pilot_dropdown.click()  
        time.sleep(1)
        print(" Landing Atul tiwari Pilot selected successfully")
        take_screenshot(driver,"Landing Pilot")

    except Exception as e:
       pytest.fail(f"Atul Tiwari is not selected for Landing Pilot")

#   Select drone

    wait = WebDriverWait(driver, 15)  # Ensure 'wait' is defined in this scope
    try:
        
        drone_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "drone")))
        drone_dropdown.click()
        time.sleep(1) 
        d001_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='drone']/option[@value='D001']"))
        )
        d001_option.click()
        # driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", drone_dropdown, "D001")
        print("Drone 'D001' is selected, UI should update now.")
        # Step 4: Wait for Next button to be visible
        next_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, ""))
        )
        next_button.click()
        print("Next button is now visible!")
        take_screenshot(driver,"Drone Selected ")

    except Exception as e:
        pytest.fail(f"Drone selection failed or Next button not visible: {e}")

    
    # try:
    #   select_drone = wait.until(EC.presence_of_element_located((By.ID, "drone")))
    #   select_drone.click()
    #   select = Select(select_drone)
    #   select.select_by_visible_text("D001")
    #   print(" D001 is selected")
    #   take_screenshot(driver, "drone_selected")
    # except Exception as e:
    #     pytest.fail(f'Drone is not selected')


    try:
    # Wait until Next button is clickable
       next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']")))
       next_btn.click()
       print(" Next Button clicked")
       take_screenshot(driver, "next_button_click")  
       time.sleep(5)  
    except Exception as e:
     pytest.fail(f" Failed to click Next button: {e}")

   #  Final create Flight  
    try:
        final_flight = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Schedule Flight']")))
        final_flight.click()
        print("Flinal Flight Create")
        take_screenshot(driver,"Final Flight")
    except Exception as e:
        pytest.fail(f'Flight not created successfully')
        
        # Complete 70/30 Task 

    




   

