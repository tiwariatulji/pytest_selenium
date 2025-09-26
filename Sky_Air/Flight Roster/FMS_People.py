import pytest
import time
import random
import string
from datetime import date, timedelta, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# Utility function to capture screenshot
def take_screenshot(driver, name):
    filename = f"screenshot/{name}.png"
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
    time.sleep(10)
    print("Logged in successfully")
    take_screenshot(driver, "login_success")
    
    # select Perosn form FMS People Section 
    
    try:
        user_data = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/fms-app/people']")))
        user_data.click()
        print("Clicked on People Section ")
        take_screenshot(driver, "FMS People Section")
        time.sleep(10)
    except Exception as e:
        pytest.fail(f"Failed to select People ")
        
    # Add new Employee
    add_new_emp = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn btn-primary addButton']")))
    add_new_emp.click()
    print('add New Epm selected')
    time.sleep(10)
    
    # Provide Access To FMS? *
    provide_access = wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[text()='No'])[1]")))
    provide_access.click()
    # assert provide_access.is_selected()
    print("Check box selected No")    
    
    # Is HOD?*
    Is_Hod = wait.until(EC.element_to_be_clickable((By.XPATH,"(//label[text()='No'])[2]")))
    Is_Hod.click()
    print("Is Hod selected No")
    
    # Select Department 
    Select_Department = driver.find_element(By.ID,"department")
    select = Select(Select_Department)
    select.select_by_visible_text("Operations : Dept002")
    print('Department is selected')
    

    # dropdown = Select(driver.find_element(By.ID, "department"))
    # dropdown.select_by_visible_text("Operations : Dept002")
    # # Optional: Assert that the correct option is selected
    # selected_option = dropdown.first_selected_option
    # assert selected_option.text.strip() == "Operations : Dept002"
   
    
    #  Personal Details
    # Generate random data
   
    try:
            
        first_names = ["manpree", "Rajeev", "Sumit", "Nikhil", "Naveen", "Rohit", "Snajeev", "Nilesh", "Mayank", "Kalpesh"]
        last_names = ["Singh", "Yadav", "Rai", "Rathore", "Panday", "Mishra", "Shukla", "Dubey", "Trivedi", "Patel"]
        random_first = random.choice(first_names)
        random_last = random.choice(last_names)
        full_name = f"{random_first} {random_last}"
        employee_code = f"{random_first} {random_last}"
        mobile = f"9{random.randint(100000000, 999999999)}"
        email = f"{random_first.lower()}{random_last.lower()}{random.randint(1,100)}@gmail.com"
        First_name = wait.until(EC.element_to_be_clickable((By.ID,"name")))
        First_name.send_keys(full_name)
        print("First Name Filed with name")
        take_screenshot(driver,"First Name Fill")

    # Employee Code *
        Employee_Code = wait.until(EC.element_to_be_clickable((By.ID,"empCode")))
        Employee_Code.send_keys(employee_code)
        print("Employee Id is Filed")
        take_screenshot(driver,"Employee_Code")
        driver.execute_script("window.scrollBy(0, 500);")


    # Mobile*
        Mobile_number = wait.until(EC.element_to_be_clickable((By.ID,"contactNumber")))
        Mobile_number.send_keys(mobile)
        print("Mobile Number is selected ")
        take_screenshot(driver, "Mobile number is Filled")

    # Email Id
        Email_id = wait.until(EC.element_to_be_clickable((By.ID,"emailAddress")))
        Email_id.send_keys(email)
        print("Email Id Selected")
        
    except Exception as e:
        pytest.fail(f" Please check Form Details EMP, MOBILE, EMAIL not slected ")
        take_screenshot(driver,'EMP MOBILE EMAIL')

   # date selected
    select_date = wait.until(EC.element_to_be_clickable((By.ID,"joiningDate")))
    current_date = date.today()
    select_date.send_keys(current_date.strftime('%d-%m-%y'))
    print(f"selected date {current_date}")
    print("Current date selected")
   

   #  select Role *    
    Select_role = driver.find_element(By.ID, "role")
    select = Select(Select_role)
    select.select_by_visible_text("Sorter : R0025")
    print("Selected Role : Shorter  ")
   
    
    # Reporting Manager *
    # try:
    #     reporting_manager = wait.until(EC.visibility_of_element_located((By.ID,"reportingManager")))
    #     select = Select(reporting_manager)
    #     driver.execute_script("arguments[0].scrollIntoView(true);",reporting_manager)
    #     select.select_by_visible_text("Abhay Raj Prajapati")
    #     print("Repoerting Manger is Selected ")
    #     take_screenshot(driver,"Reporting Manager Selected ")
    #     time.sleep(10)
    # except Exception as e:
    #     pytest.fail(f"Reporting Mangrer is not selected")
    #     take_screenshot(driver,"Manager is not selected")
    # Wait until dropdown is present
    try:
        reporting_manager = wait.until(
            EC.presence_of_element_located((By.ID, "reportingManager"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", reporting_manager)
        time.sleep(1)
        select = Select(reporting_manager)
        # Wait until options are loaded (more than just 'Select...')
        wait.until(lambda d: len(select.options) > 1)
        # Debug: print all options
        options = [opt.text.strip() for opt in select.options]
        print("Dropdown options found:", options)
        # Target option
        target_name = "Abhay Raj Prajapati"
        # Try selecting target
        if target_name in options:
            select.select_by_visible_text(target_name)
            print(f"Reporting Manager '{target_name}' is selected successfully")
            take_screenshot(driver, "Reporting_Manager_Selected")
        else:
            take_screenshot(driver, "Manager_Option_Not_Found")
            pytest.fail(f"Option '{target_name}' not found in dropdown. Available: {options}")

        time.sleep(2)
    except Exception as e:
        take_screenshot(driver, "Manager_Not_Selected")
        pytest.fail(f"Reporting Manager selection failed due to: {e}")
        
    # 