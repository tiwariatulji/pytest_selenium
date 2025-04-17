# #  Helathians Coupon 

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.chrome.service import Service


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://devcrm027.echl.co.in/manage/bookings")
# time.sleep(2)
# # Locate the coupon code element using XPath
# print(driver.title)
 
# # username
# username = driver.find_element(By.NAME, value="username")
# username.send_keys("atul.tiwari@healthians.com")
# time.sleep(2)

# # password
# password = driver.find_element(By.NAME, value="password")
# password.send_keys("Atul@1234")
# time.sleep(2)

# # Remember me checkbox
# remember_me = driver.find_element(By.XPATH, value="//label/input[@type='checkbox']")
# remember_me.click()
# time.sleep(2)

# # click on the login button
# login_button = driver.find_element(By.ID, value="login_submit")
# login_button.click()
# time.sleep(10)

# ----------------------- Helathians Coupon -----------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta

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
driver.get("https://devcrm027.echl.co.in/manage/bookings")
time.sleep(2)

# Print the page title
print(driver.title)

# Username field
username = driver.find_element(By.NAME, value="username")
username.send_keys("atul.tiwari@healthians.com")
time.sleep(2)

# Password field
password = driver.find_element(By.NAME, value="password")
password.send_keys("Atul@1234")
time.sleep(2)

# Remember me checkbox
remember_me = driver.find_element(By.XPATH, value="//label/input[@type='checkbox']")
remember_me.click()
time.sleep(2)

# Login button
login_button = driver.find_element(By.ID, value="login_submit")
login_button.click()

# Wait to observe logged-in state
time.sleep(10)

# search coupon name on input field
search_coupon = driver.find_element(By.ID, value="searchSidebarAction")
search_coupon.send_keys("coupon")
time.sleep(5)

# click on Coupon Management 
marketing_element = driver.find_element(By.XPATH, "//span[@class='actionGroupTitle' and contains(text(), 'Marketing')]")
marketing_element.click()
time.sleep(5)

# click on Campaign Coupon Management
wait = WebDriverWait(driver, 10) # Wait for the element to be clickable
coupon_mangement = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Campaign Coupon Management']")))
coupon_mangement.click()
time.sleep(20)

# add coupon Campain 
add_campain= driver.find_element(By.XPATH, "//a[@title='New Campaign']//i[@class='fa fa-plus']")
add_campain.click()
time.sleep(5)

# Create Campaign Coupon Form 
cmapain_name = driver.find_element(By.NAME, value="campaign")
cmapain_name.send_keys("Atul_Task")

frequency = driver.find_element(By.ID, value="frequency")
frequency.send_keys("100")
time.sleep(10)


# Enter Campaign Start Date
# campaign_start_input = driver.find_element(By.XPATH, "//input[@id='datepicker1']")
# campaign_start_input.clear()
# campaign_start_input.send_keys("2025-05-01")

# # Enter Campaign End Date
# campaign_end_input = driver.find_element(By.XPATH, "//input[@placeholder='Campaign End Date']")
# campaign_end_input.clear()
# campaign_end_input.send_keys("2025-05-31")
# Find and click on the start date input

# wait = WebDriverWait(driver, 5)

# # Step 1: Click on the date input field
# date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='datepicker1']")))  # Adjust ID if different
# date_input.click()

# # Step 2: Select today's date from the calendar
# today_date = datetime.now().day
# today_locator = f"//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{today_date}']"

# # Wait for the date to be clickable and click it
# wait.until(EC.element_to_be_clickable((By.XPATH, today_locator))).click()

wait = WebDriverWait(driver, 10)

# ====== Step 1: Select Campaign Start Date ======
start_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='datepicker1']")))  # Adjust ID if needed
start_date_input.click()

today = datetime.today()
today_day = today.day

# Click today's date in calendar
today_xpath = f"//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{today_day}']"
wait.until(EC.element_to_be_clickable((By.XPATH, today_xpath))).click()

# ====== Step 2: Select Campaign End Date (today + 10 days) ======
end_date_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='datepicker2']")))  # Adjust ID if needed
end_date_input.click()

end_day = (today + timedelta(days=10)).day
end_month = (today + timedelta(days=10)).month
end_year = (today + timedelta(days=10)).year

# If end date falls in next month/year, you may need to navigate the calendar forward
# Simple example assumes same month
end_xpath = f"//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{end_day}']"
wait.until(EC.element_to_be_clickable((By.XPATH, end_xpath))).click()


# ====== Step 2: Sample Collection Start Date: ======
wait = WebDriverWait(driver, 5)

# ====== Step 2: Select Campaign Start Date ======
sample_collection_start = wait.until(EC.element_to_be_clickable((By.ID, "sample_collection_start_date")))  # Adjust ID if needed
sample_collection_start.click()

today = datetime.today()
today_day = today.day

# Click today's date in calendar
today_xpath = f"//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{today_day}']"
wait.until(EC.element_to_be_clickable((By.XPATH, today_xpath))).click()

# ====== Step 2: Select Campaign End Date (today + 10 days) ======
end_date_input = wait.until(EC.element_to_be_clickable((By.ID, "sample_collection_end_date")))  # Adjust ID if needed
end_date_input.click()

end_day = (today + timedelta(days=10)).day
end_month = (today + timedelta(days=10)).month
end_year = (today + timedelta(days=10)).year

# If end date falls in next month/year, you may need to navigate the calendar forward
# Simple example assumes same month
end_xpath = f"//td[not(contains(@class,'ui-datepicker-other-month'))]/a[text()='{end_day}']"
wait.until(EC.element_to_be_clickable((By.XPATH, end_xpath))).click()




# Wait a moment to see the results
time.sleep(3)



# Optional: close the browser
# driver.quit()



