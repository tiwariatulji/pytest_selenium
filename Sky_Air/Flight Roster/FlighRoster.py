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

# Flight Roster Flow

# Wait for the button to be clickable before clicking
try:
    New_Flight = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator schedule-btn mat-button mat-button-base'])[1]"))
    )
    New_Flight.click()
    print("Clicked on Manual Flight Selection")
    time.sleep(10)
except Exception as e:
    print(f"Error finding or clicking the flight button: {e}")
    print("Page source around the error:")
    # print(driver.page_source[:2000])  # Print first 2000 chars of page source for debugging

# Wait for the manual flight button to be clickable
try:
    manual_flight = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Schedule Flight Manually']"))
    )
    manual_flight.click()
    print("Clicked on Manual Flight")
    time.sleep(5)
except Exception as e:
    print(f"Error finding or clicking the manual flight button: {e}")
    print("Page source around the error:")
    print(driver.page_source[:2000])

# Search Skye Tunnel
try:
    search_tunnel = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder=\"Search for tunnel by it's name/location\"]"))
    )
    search_tunnel.send_keys("FlipKart")
    print("Tunnel Selected")
    time.sleep(5)
except Exception as e:
    print(f"Error finding tunnel name or element not target: {e}")
   
# Select the Tunne and Create a Tunnel
try:
    Filpkart_tunnel = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='white-text f-14'][normalize-space()='Flipkart'])[1]"))
    )
    Filpkart_tunnel.click()
    print("Clicked on Flipkart Tunnel")
    time.sleep(5)
except Exception as e:
    print(f"Error finding or clicking the Flipkart tunnel: {e}")


# select the schedule Delivery

schedule_Delivery = driver.find_element(By.XPATH, value="//button[@class='btn primary-btn f-12 py-2']")
schedule_Delivery.click()
print("Clicked on Schedule Delivery")
time.sleep(5)

# Wait for date input and click to open calendar
wait = WebDriverWait(driver, 2)
date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='exampleFormControlInput1']")))
date_input.click()
# Get tomorrow's date
tomorrow = date.today() + timedelta(days=1)
formatted_date = f"{tomorrow.day:02d}-{tomorrow.month:02d}-{tomorrow.year}"
date_input.send_keys(formatted_date)
print("Selected tomorrow's date:", formatted_date)
time.sleep(5)
# Select Delivery Count
how_many = driver.find_element(By.XPATH, value="//select[@aria-label='Default select example']")
select_object = Select(how_many)
select_object.select_by_visible_text("1")
print("Selected 1 Delivery")


# Select 1st Slot for Flight
try:
    wait = WebDriverWait(driver, 5)
    slot_select = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-dark time-btn br-15 f-12 fw-bold ng-star-inserted'])[2]")))
    slot_select.click()
    print("Selected 1st Slot for Flight")
    time.sleep(5)
except Exception as e:
    print(f"Error selecting the 1st  slot: {e}")

# Sltot Selection
try:
    slot_selection = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-dark slottime-btn br-15 f-12 fw-bold']"))
    )
    slot_selection.click()
    print("Clicked on Slot Slection button")
    time.sleep(5)

except Exception as e:
    print(f"Test failed due to: Slot seletion is not completed {e}")

# TIme Slot Selection
try:
    #  Wait for the time field
    time_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='time' and @formcontrolname='timeSlot']"))
    )

    #  set 22:00 dynamically
    selected_time = datetime.strptime("22:00", "%H:%M").strftime("%H:%M")

    #  Clear and enter time
    # time_input.clear()
    time_input.send_keys(selected_time)

    #  Click slot button after time is selected
    slot_selection = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='time' and @formcontrolname='timeSlot']"))
    )
    slot_selection.click()
    time.sleep(5)

    print(f" Time slot selected: {selected_time}")

except Exception as e:
    print(f" Error selecting the time slot: Slot could not be slectd {e}")


# Slect show time Slot 
select_time_slot = driver.find_element(By.XPATH, value="(//button[@class='btn btn-dark time-btn br-15 f-12 fw-bold ng-star-inserted'])[1]")
select_time_slot.click()
print("Clicked on Show Time Slot Button")

# Next Button click
next_button_1 = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn primary-btn f-12 py-2']"))
    )
next_button_1.click()
print("Clicked on Next Button after selecting time slot")
time.sleep(10)

# Client Organization Selection
try:
    organization = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class, 'form-select')]"))
        )
    select_object = Select(organization)
    select_object.select_by_visible_text("ECOM")
    print("Selected Organization")
    time.sleep(5)
except Exception as e:
    print(f"Error selecting organization: {e}")

# Client Name Selection
try:
    # Wait for at least 2 select elements with form-select class
    WebDriverWait(driver, 5).until(
        lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 2
    )
    # Get all select elements
    selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
    # The second select is for client name
    Client_Name = selects[1]
    select_object = Select(Client_Name)
    # Wait for options to load
    WebDriverWait(driver, 10).until(
        lambda driver: len(select_object.options) > 1
    )
    select_object.select_by_visible_text("Abhinav Dhiman")
    print("Selected Client Name")
    time.sleep(5)
except Exception as e:
    print(f"Error selecting Client: client name not selected {e}")

# TakeOff Pilot - Location 1
try:
    # Wait for at least 3 select elements with form-select class
    WebDriverWait(driver, 5).until(
        lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 3
    )
    # Get all select elements
    selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
    # The third select is for takeoff pilot
    TakeOff_Pilot = selects[2]
    select_object = Select(TakeOff_Pilot)
    # Wait for options to load
    WebDriverWait(driver, 5).until(
        lambda driver: len(select_object.options) > 1
    )
    select_object.select_by_visible_text("Animesh Verma")
    print("Selected TakeOff Pilot Animesh Verma")
    time.sleep(5)
except Exception as e:
    print(f"Error selecting TakeOff Pilot: {e}")

# # Landing Pilot - Location 2 
try:
    # Wait for at least 3 select elements with form-select class
    WebDriverWait(driver, 5).until(
        lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 4
    )
    # Get all select elements
    selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
    # The third select is for takeoff pilot
    TakeOff_Pilot = selects[3]
    select_object = Select(TakeOff_Pilot)
    # Wait for options to load
    WebDriverWait(driver, 5).until(
        lambda driver: len(select_object.options) > 2
    )
    select_object.select_by_visible_text("Tarun Sadhya")
    print("Selected Landing Pilot Tarun Sadhya")
    time.sleep(5)
except Exception as e:
    print(f"Error selecting TakeOff Pilot: Take off Pilot Not selcted {e}")


try:
    # Wait for at least 3 select elements with form-select class
    WebDriverWait(driver, 5).until(
        lambda driver: len(driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")) >= 5
    )
    # Get all select elements
    selects = driver.find_elements(By.XPATH, "//select[contains(@class, 'form-select')]")
    # The third select is for takeoff pilot
    TakeOff_Pilot = selects[4]
    select_object = Select(TakeOff_Pilot)
    # Wait for options to load
    WebDriverWait(driver, 5).until(
        lambda driver: len(select_object.options) > 2
    )
    select_object.select_by_visible_text("Hexo One")
    print("Dron Slected Hexo One")
    time.sleep(5)
except Exception as e:
    print(f"Error selecting Drone Selection: Drone not selcted {e}")

except Exception as e:
    print(f"Error selecting organization: {e}")

# Submit the Clint Details Form
Next_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn primary-btn f-12 py-2']"))
    )
Next_button.click()
print("Clicked on Next Button after selecting time slot")
time.sleep(10)

# selcect time slot after client details
time_select = driver.find_element(By.XPATH, value="//span[@class='time-active btn btn-dark']")
time_select.click()
print("Clicked on Time Slot After Client Details")
time.sleep(5)

# check box click
try:
    check_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'checkbox-position')]"))
    )
    check_box.click()
    print("Clicked on Check Box")
except Exception as e:
    print(f"Error finding or clicking the checkbox: {e}")

# Proceed to Overview
try:
    proceed_overview = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn primary-btn')]"))
    )
    proceed_overview.click()
    print("Clicked on Proceed to Overview Button")
    time.sleep(2)
except Exception as e:
    print(f"Error finding or clicking the proceed overview button: {e}")

try:
#  final Submit for Flight Booking
   final_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()=' Confirm my order ']"))
    )
   final_submit.click()
   print("Clicked on Final Submit Button Flight Booked Successfully")
   time.sleep(15)
except Exception as e:
    print(f"Error finding or clicking the final submit button: {e}")

# done for Now 
try:    
    done_for_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-dark-border btn-hover btn-block f-12 py-2']"))
    )
    done_for_now.click()
    print("Clicked on Done for Now Button")
    time.sleep(15)   
except Exception as e:
    print(f"Error finding or clicking the done for now button: {e}")

# Return to Flight Roster Page

return_flight_roster = driver.find_element(By.XPATH, value="//span[text()='Flight Roster']")
return_flight_roster.click()
time.sleep(10)
print("Clicked on Flight Roster Page ")

# Approve the Flight
Approve_flight = driver.find_element(By.XPATH, value="(//button[@class='mat-focus-indicator approve-btn mat-button mat-button-base'])[1]")  
Approve_flight.click()
print("Clicked on Approve Flight Button")

