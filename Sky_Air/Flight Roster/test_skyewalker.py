# import pytest
# import os
# import time
# from datetime import datetime, timedelta, date
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# def test_skyewalker_attendance():
#     """Simple pytest version of your original script"""
    
#     # Create screenshots directory
#     screenshots_dir = "screenshots"
#     os.makedirs(screenshots_dir, exist_ok=True)
    
#     def take_screenshot(name, status="pass"):
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"{status}_{name}_{timestamp}.png"
#         filepath = os.path.join(screenshots_dir, filename)
#         driver.save_screenshot(filepath)
#         print(f"Screenshot: {filename}")
    
#     # Chrome Options for Allowing Notification
#     chrome_options = Options()
#     prefs = {
#         "profile.default_content_setting_values.notifications": 1  # 1 = Allow, 2 = Block
#     }
#     chrome_options.add_experimental_option("prefs", prefs)
    
#     # Launch Chrome with options
#     driver = webdriver.Chrome(options=chrome_options) 
#     driver.maximize_window()
    
#     try:
#         # Open the target URL
#         driver.get("https://uat.skyeairops.tech/operator/cod")
#         time.sleep(2)
        
#         # Print the page title
#         print(driver.title)
        
#         username = driver.find_element(By.ID, value="emailId")
#         username.send_keys("atul.tiwari@skyeair.tech")
#         time.sleep(2)
#         take_screenshot("enter_username", "pass")
#         print("PASS: Username entered")
        
#         # Password field
#         password = driver.find_element(By.ID, value="floatingPassword")
#         password.send_keys("Atul@123")
#         time.sleep(2)
#         take_screenshot("enter_password", "pass")
#         print("PASS: Password entered")
        
#         # Login 
#         Login = driver.find_element(By.XPATH, '//button[@type="submit"]')
#         Login.click()
#         time.sleep(10)
#         take_screenshot("click_login", "pass")
#         print("PASS: Login clicked")
        
#         # Select on SkyeWalker Mapping
#         wait = WebDriverWait(driver, 20) 
#         try:
#             Skye_wlaker = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "(//span[@class='f-14 px-1'])[2]"))
#             )
#             Skye_wlaker.click()
#             print("PASS: Clicked on SkyeWalker Section")
#             take_screenshot("click_skyewalker", "pass")
#             time.sleep(5)
#         except Exception as e:
#             print(f"FAIL: Error clicking on SkyeWalker section: {e}")
#             take_screenshot("click_skyewalker", "failure")
#             assert False, f"SkyeWalker section click failed: {e}"
        
#         # Attendance Selection 
#         try:
#             Attendance = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, '//div[text() ="Attendance"]'))
#             )   
#             Attendance.click()
#             print("PASS: Clicked on Attendance Dropdown")
#             take_screenshot("click_attendance", "pass")
#             time.sleep(2)
#         except Exception as e:
#             print(f"FAIL: Error clicking on Attendance Dropdown: {e}")
#             take_screenshot("click_attendance", "failure")
#             assert False, f"Attendance dropdown click failed: {e}"
        
#         # Attendance Hub selection 
#         try:
#             Attendance_hub = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "(//span[@class='icon'])[1]"))
#             )
#             Attendance_hub.click()
#             print("PASS: Clicked on Attendance Hub Dropdown")
#             take_screenshot("click_attendance_hub", "pass")
#             time.sleep(2)
#         except Exception as e:
#             print(f"FAIL: Error clicking on Attendance Hub Dropdown: {e}")
#             take_screenshot("click_attendance_hub", "failure")
#             assert False, f"Attendance Hub dropdown click failed: {e}"
        
#         # scroll until the element is visible
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
        
#         # Open Hub80 for Attendance
#         try:
#             Hub80 = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "//div[text()='Hub 80']"))
#             )
#             Hub80.click()
#             print("PASS: Clicked on Hub 80 for Attendance")
#             take_screenshot("select_hub80", "pass")
#             time.sleep(5)   
#         except Exception as e:
#             print(f"FAIL: Error clicking on Hub 80 for Attendance: {e}")
#             take_screenshot("select_hub80", "failure")
#             assert False, f"Hub 80 selection failed: {e}"
        
#         hub_name = driver.find_element(By.XPATH, "(//div[@class='circle'])[1]")
#         hub_name.click()
#         time.sleep(2)
#         take_screenshot("click_hub_name", "pass")
#         print("PASS: Hub name clicked")
        
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
        
#         # Selected User Name for Attendance
#         try:
#             user_name = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "(//a[@class='white-text'])[3]"))
#             )
#             user_name.click()
#             print("PASS: Clicked on User Name for Attendance")
#             take_screenshot("select_user", "pass")
#             time.sleep(5)
#         except Exception as e:
#             print(f"FAIL: Error clicking on User Name for Attendance: {e}")
#             take_screenshot("select_user", "failure")
#             assert False, f"User selection failed: {e}"
        
#         # select the date picker
#         date_picker = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.XPATH, "(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[2]"))
#             )
#         date_picker.click()
#         time.sleep(2)
#         print("PASS: Clicked on Date Picker")
#         take_screenshot("open_date_picker", "pass")
        
#         today = date.today()
#         dates_to_select = [today, today + timedelta(days=1)]  # Today and tomorrow
        
#         for future_date in dates_to_select:
#             day = future_date.day
#             try:
#                 date_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//td//button[normalize-space()='{day}']")))
#                 date_button.click()
#                 print(f"PASS: Selected Date: {future_date}")
#                 take_screenshot(f"select_date_{future_date}", "pass")
#                 time.sleep(1)
#             except:
#                 print(f"FAIL: Date {future_date} not found in date picker")
#                 take_screenshot(f"select_date_{future_date}", "failure")
        
#         time.sleep(2)
        
#         # search Filter data 
#         search_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary f-12 m-2 ng-star-inserted']")))
#         search_filter.click()
#         print("PASS: Clicked on Search Filter")
#         take_screenshot("search_filter", "pass")
#         time.sleep(2)
        
#         # Filter Reset Button
#         reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-danger f-12 m-2 ng-star-inserted']")))
#         reset_button.click()
#         print("PASS: Clicked on Reset Button")
#         take_screenshot("reset_button", "pass")
#         time.sleep(2)
        
#         # Export User Data
#         export_data = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary f-12 m-2']")))
#         export_data.click()
#         print("PASS: Clicked on Export User Data")
#         take_screenshot("export_data", "pass")
#         time.sleep(5)
        
#         # Close the User History tab
#         close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space()='close']")))
#         close_tab.click()   
#         print("PASS: Clicked on Close Tab")
#         take_screenshot("close_tab", "pass")
#         time.sleep(2)
        
#         # Return Home Page
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#         take_screenshot("complete_test", "pass")
#         print("PASS: Test completed successfully")
        
#     except Exception as e:
#         take_screenshot("test_error", "failure")
#         print(f"FAIL: Test failed with error: {e}")
#         raise
#     finally:
#         driver.quit()


# if __name__ == "__main__":
#     # Run with pytest and generate HTML report
#     import subprocess
#     import sys
    
#     cmd = [
#         "python", "-m", "pytest", __file__, 
#         "-v", "-s", 
#         "--html=reports/report.html", 
#         "--self-contained-html"
#     ]
    
#     os.makedirs("reports", exist_ok=True)
#     subprocess.run(cmd)




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

def test_skye_attendance(driver):
    wait = WebDriverWait(driver, 15)

    # Step 1: Open URL
    driver.get("https://uat.skyeairops.tech/operator/cod")
    time.sleep(2)
    # assert "COD" in driver.title, " Page title not matched"
    print(" Opened URL successfully")
    take_screenshot(driver, "open_url")

    # Step 2: Login
    driver.find_element(By.ID, "emailId").send_keys("atul.tiwari@skyeair.tech")
    driver.find_element(By.ID, "floatingPassword").send_keys("Atul@123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    # assert "Dashboard" in driver.page_source, " Login failed"
    print(" Logged in successfully")
    take_screenshot(driver, "login_success")

    # Step 3: Click SkyeWalker Mapping
    try:
        skye_walker = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='f-14 px-1'])[2]")))
        skye_walker.click()
        print("Clicked on SkyeWalker Section")
        take_screenshot(driver, "skye_walker_section")
    except Exception as e:
        pytest.fail(f" Failed to click SkyeWalker: {e}")

    # Step 4: Attendance Selection
    try:
        attendance = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text() ="Attendance"]')))
        attendance.click()
        print("Clicked Attendance Dropdown")
        take_screenshot(driver, "attendance_dropdown")
    except Exception as e:
        pytest.fail(f" Attendance Dropdown not clickable: {e}")

    # Step 5: Attendance Hub Selection
    try:
        hub_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='icon'])[1]")))
        hub_dropdown.click()
        print(" Clicked Attendance Hub Dropdown")
        take_screenshot(driver, "hub_dropdown")
    except Exception as e:
        pytest.fail(f" Hub dropdown not clickable: {e}")

    # Step 6: Open Hub 80
    try:
        hub80 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Hub 80']")))
        hub80.click()
        print(" Clicked on Hub 80")
        take_screenshot(driver, "hub_80")
    except Exception as e:
        pytest.fail(f" Failed to select Hub 80: {e}")

    # Step 7: Select User Name
    try:
        user_name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='white-text'])[3]")))
        user_name.click()
        print(" Clicked on User Name")
        take_screenshot(driver, "user_name")
    except Exception as e:
        pytest.fail(f" User name not clickable: {e}")
        

    # Step 8: Select Dates (Today & Tomorrow)
    try:
        date_picker = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@class='mat-focus-indicator mat-icon-button mat-button-base'])[2]")))
        date_picker.click()
        print(" Opened Date Picker")
        take_screenshot(driver, "date_picker")

        today = date.today()
        dates_to_select = [today, today + timedelta(days=1)]
        for future_date in dates_to_select:
            day = future_date.day
            date_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//td//button[normalize-space()='{day}']"))
            )
            date_button.click()
            print(f" Selected Date: {future_date}")
            take_screenshot(driver, f"date_{day}")

    except Exception as e:
        pytest.fail(f" Date selection failed: {e}")

    # Step 9: Search Filter
    search_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary f-12 m-2 ng-star-inserted']")))
    search_filter.click()
    print(" Clicked Search Filter")
    take_screenshot(driver, "search_filter")

    # Step 10: Reset Button
    reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-danger f-12 m-2 ng-star-inserted']")))
    reset_button.click()
    print(" Clicked Reset Button")
    take_screenshot(driver, "reset_button")

    # Step 11: Export Data
    export_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary f-12 m-2']")))
    export_button.click()
    print(" Exported User Data")
    take_screenshot(driver, "export_data")

    # Step 12: Close Tab
    close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space()='close']")))
    close_tab.click()
    print("Closed Tab Successfully")
    take_screenshot(driver, "close_tab")
