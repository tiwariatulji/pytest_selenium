from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
driver.get("https://www.skyeair.tech/")
# // print the page title
print("Page Title:", driver.title)
assert "Sky" in driver.title or "Air" in driver.title  # Adjust based on
time.sleep(2)

# Home Page
print(" Page loaded successfully.")

# Click on "Delivery with Us Today"
try:
    wait = WebDriverWait(driver, 10)
    delivery_today = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='delivery-text']")))
    delivery_today.click()
    print(" Delivery with Us Today clicked.")
except:
    print(" Delivery with Us Today element not found.")

time.sleep(2)

# Validation logic before submitting form
errors = []

# Fill and validate form inputs
try:
    first_name = driver.find_element(By.XPATH, "//input[@id ='«r0»']")
    if first_name.get_attribute("value").strip() == "":
        first_name.send_keys("Atul")
    if first_name.get_attribute("value").strip() == "":
        errors.append("First Name is required.")
except:
    errors.append("First Name field not found.")

try:
    last_name = driver.find_element(By.XPATH, "//input[@id ='«r1»']")
    if last_name.get_attribute("value").strip() == "":
        last_name.send_keys("Tiwari")
    if last_name.get_attribute("value").strip() == "":
        errors.append("Last Name is required.")
except:
    errors.append("Last Name field not found.")

try:
    email = driver.find_element(By.XPATH, "//input[@id ='«r2»']")
    if email.get_attribute("value").strip() == "":
        email.send_keys("atul@example.com")
    if email.get_attribute("value").strip() == "":
        errors.append("Email is required.")
except:
    errors.append("Email field not found.")

try:
    mobile = driver.find_element(By.XPATH, "//input[@id ='«r3»']")
    if mobile.get_attribute("value").strip() == "":
        mobile.send_keys("9999999999")
    if mobile.get_attribute("value").strip() == "":
        errors.append("Mobile number is required.")
except:
    errors.append("Mobile number field not found.")

try:
    message = driver.find_element(By.NAME, "Message")
    if message.get_attribute("value").strip() == "":
        message.send_keys("Looking to partner with you for drone delivery.")
    if message.get_attribute("value").strip() == "":
        errors.append("Message is required.")
except:
    errors.append("Message field not found.")


# Print validation result or submit the form
if errors:
    print(" Validation failed:")
    for err in errors:
        print(f" - {err}")
else:
    submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit_button.click()
    print(" Form submitted successfully.")
    print(" Test Passed!")

try:
    close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
    close_popup.click()
    print("Popup closed successfully.")
except Exception as e:
    print("No popup found or failed to close:", e)    

scroll_pause_time = 1  # seconds

# Get the total scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down by window height
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(scroll_pause_time)

    # Calculate new scroll height
    new_height = driver.execute_script("return window.pageYOffset + window.innerHeight")

    if new_height >= last_height:
        break
FAQ = driver.find_element(By.XPATH, '//span[text()="What is Skye Air and how does drone delivery work?"]')
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", FAQ)
time.sleep(1)
driver.execute_script("arguments[0].click();", FAQ)
print("FAQ button clicked.")
time.sleep(5)

# FAQ 2 Answer
FAQ2 = driver.find_element(By.XPATH, '//span[text()="Which areas or cities in India does Skye Air currently operate in?"]')
FAQ2.click()
print("FAQ 2 button clicked.")
time.sleep(2)
# FAQ 3 Answer
FAQ3 = driver.find_element(By.XPATH, '//span[text()="What types of goods can be delivered using Skye Air drones?"]')
FAQ3.click()
print("FAQ 3 button clicked.")
time.sleep(2)


time.sleep(5)
driver.quit()
# Close the browser
print("Browser closed.")