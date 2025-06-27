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
time.sleep(10)

# Home Page
print(" Page loaded successfully.")

# # Dilevery with Us Toady on the Home Page
# wait = WebDriverWait(driver, 10)
# delivery_today = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='delivery-text']")))
# delivery_today.click()
# time.sleep(2)
# # print(driver.page_source)  // Print the page source to verify navigation
# print(" Delivery with Us Today clicked.")

# # Delivery with us contct page
# wait = WebDriverWait(driver, 10)
# contact_us = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id ='«r0»']")))
# contact_us.send_keys("Atul")
# print(" Contact Us field filled with 'Atul'.")
# time.sleep(1)

# # Last Name Field
# last_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id ='«r1»']")))
# last_name.send_keys("Tiwari")
# print(" Last Name field filled with 'Tiwari'.")
# time.sleep(1)

# # Email Field
# email = driver.find_element(By.XPATH, "//input[@id ='«r2»']")
# email.send_keys("atul.tiwari@skyeair.tech")
# print(" Email field filled with 'atul.tiwari@skyeair.tech'.")
# time.sleep(1)

# # / mobile Number Field
# mobile_number = driver.find_element(By.XPATH, "//input[@id ='«r3»']")
# mobile_number.send_keys("1234567890")
# print(" Mobile Number field filled with '1234567890'.")
# time.sleep(1)

# # Message Field
# message = driver.find_element(By.NAME, "Message")
# message.send_keys("I want to schedule a flight for my Pacakge.")
# print("Message field filled with 'I want to schedule a flight for my Package.'.")  
# time.sleep(1)

# # Submit Button
# submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")  
# submit_button.click()
# print("Submit button clicked.")
# time.sleep(1)



# # close the Popup
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
#     close_popup.click()
#     print("Popup closed successfully.")
# except Exception as e:
#     print("No popup found or failed to close:", e)

# Scroll down the page to load more content

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
# driver.quit()  # Close the browser after completion
# print("Browser closed.")