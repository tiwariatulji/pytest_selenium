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

# Select on SkyeWalker Mapping
wait = WebDriverWait(driver, 20) 
try:
    Skye_wlaker = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='f-14 px-1'])[2]"))
    )
    Skye_wlaker.click()
    print("Clicked on SkyeWalker Section")
    driver.save_screenshot("skye_walker_section.png")
    time.sleep(5)
    # take_screenshot(driver, "skye_walker_section")
except Exception as e:
    print(f"Error clicking on SkyeWalker section: Skye Walker Not slected  {e}")
# raise Exception("Stopping execution due to failure in clicking SkyeWalker section.")

# Attendance Selection 
try:
    Attendance = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[text() ="Attendance"]'))
    )   
    Attendance.click()
    print(" Status : Clicked on Attentence Dropdown")

    time.sleep(2)
except Exception as e:
    print(f"Error clicking on Attentence Scrollbar: {e}")
    raise
Exception("Stopping execution due to failure in clicking Attentence Scrollbar.")

# Attendance Hub slection 
try:
    Attendance_hub = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='icon'])[1]"))
    )
    Attendance_hub.click()
    print("Clicked on Attentence Hub Dropdown")
    time.sleep(2)
except Exception as e:
    print(f"Error clicking on Attentence Hub Dropdown: {e}")
    # raise Exception("Stopping execution due to failure in clicking Attentence Hub Dropdown.")

# scroll untill the element is visible
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Open Hub80 for Attendance
try:
    Hub80 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Hub 80']"))
    )
    Hub80.click()
    print("Clicked on Hub 89 for Attendance")
    time.sleep(5)   
except Exception as e:
    print(f"Error clicking on Hub 80 for Attendance: {e}")
    # raise Exception("Stopping execution due to failure in clicking Hub 80 for Attendance.")   


hub_name = driver.find_element(By.XPATH, "(//div[@class='circle'])[1]")
hub_name.click()
time.sleep(2)
# print("Hub Name is:", hub_name.text)
# if hub_name.text == "Hub 89":
#     print("Hub 80 is selected for Attendance")
#     # driver.save_screenshot("hub_80_attendance.png")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Selected User Name for Attendance
try:
    user_name = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//a[@class='white-text'])[3]"))
    )
    user_name.click()
    print("Clicked on User Name for Attendance")
    time.sleep(5)
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)
except Exception as e:
    print(f"Error clicking on User Name for Attendance: {e}")


# select the date picker
date_picker = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[2]"))
    )
# date_picker = WebDriverWait(driver, 20) (EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[2]")))
date_picker.click()
time.sleep(2)
print("Clicked on Date Picker")

today = date.today()
dates_to_select = [today, today + timedelta(days=1)]  # Today and tomorrow

for future_date in dates_to_select:
    day = future_date.day
    try:
        date_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//td//button[normalize-space()='{day}']")))
        date_button.click()
        print(f"Selected Date: {future_date}")
        time.sleep(1)
    except:
        print(f"Date {future_date} not found in date picker")

time.sleep(2)


# search Filter data 
search_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary f-12 m-2 ng-star-inserted']")))
search_filter.click()
print("Clicked on Search Filter")
time.sleep(2)

# Filter Reset Button
reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-danger f-12 m-2 ng-star-inserted']")))
reset_button.click()
print("Clicked on Reset Button")
time.sleep(2)

# Export User Data
export_data = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary f-12 m-2']")))
export_data.click()
print("Clicked on Export User Data")
time.sleep(5)

# Close the User History tab
close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space()='close']")))
close_tab.click()   
print("Clicked on Close Tab")
time.sleep(2)

# Return Home Page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)



