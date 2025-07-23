from ast import Await
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

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
driver.get("https://uat.skyeair.tech/home")
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
# time.sleep(5)
# # print(driver.page_source)  // Print the page source to verify navigation
# print(" Delivery with Us Today clicked.")

# # Delivery with us contct page
# wait = WebDriverWait(driver, 10)
# contact_us = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id ='«r0»']")))
# contact_us.send_keys("Atul")
# print(" Contact Us field filled with 'Atul'.")
# time.sleep(5)

# # Last Name Field
# last_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id ='«r1»']")))
# last_name.send_keys("Tiwari")
# print(" Last Name field filled with 'Tiwari'.")
# time.sleep(2)

# # Email Field
# email = driver.find_element(By.XPATH, "//input[@id ='«r2»']")
# email.send_keys("atul.tiwari@skyeair.tech")
# print(" Email field filled with 'atul.tiwari@skyeair.tech'.")
# time.sleep(2)

# # / mobile Number Field
# mobile_number = driver.find_element(By.XPATH, "//input[@id ='«r3»']")
# mobile_number.send_keys("1234567890")
# print(" Mobile Number field filled with '1234567890'.")
# time.sleep(2)

# # Message Field
# message = driver.find_element(By.NAME, "Message")
# message.send_keys("I want to schedule a flight for my Pacakge.")
# print("Message field filled with 'I want to schedule a flight for my Package.'.")  
# time.sleep(2)

# # Submit Button
# submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")  
# submit_button.click()
# print("Submit button clicked.")
# time.sleep(5)



# # close the Popup
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
#     close_popup.click()
#     print("Popup closed successfully.")
# except Exception as e:
#     print("No popup found or failed to close:", e)

# ----------

# Scroll to the bottom of the page to ensure all elements are loaded
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


# print(" Scroll completed.")

FAQ = driver.find_element(By.XPATH, '//span[text()="What is Skye Air and how does drone delivery work?"]')
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", FAQ)
time.sleep(1)
driver.execute_script("arguments[0].click();", FAQ)
print("FAQ button clicked.")
time.sleep(1)

# FAQ 2 Answer
FAQ2 = driver.find_element(By.XPATH, '//span[text()="Which areas or cities in India does Skye Air currently operate in?"]')
FAQ2.click()
print("FAQ 2 button clicked.")

# FAQ 3 Answer
FAQ3 = driver.find_element(By.XPATH, '//span[text()="What types of goods can be delivered using Skye Air drones?"]')
FAQ3.click()
print("FAQ 3 button clicked.")
time.sleep(3)


faq4_xpath = '//span[text()="How is drone delivery different from traditional logistics services?"]'
faq4_answer_xpath = '//p[contains(text(), "Drone delivery is faster")]'

# Click FAQ 4
try:
    faq4 = wait.until(EC.element_to_be_clickable((By.XPATH, faq4_xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq4)
    time.sleep(1)
    faq4.click()
    print("FAQ Button 4 clicked.")
    time.sleep(2)
except Exception as e:
    print("Failed to click FAQ 4:", e)

# Get FAQ 4 Answer
try:
    faq4_answer = Await.until(EC.visibility_of_element_located((By.XPATH, faq4_answer_xpath)))
    print("FAQ 4 Answer:")
    print(faq4_answer.text)
except Exception as e:
    print("Could not find FAQ 4 Answer:", e)

# XPath for the FAQ question and answer
faq_question_xpath_2 = '//span[contains(text(), "Is drone delivery safe and approved by Indian aviation authorities?")]'
faq_answer_xpath_2   = '//p[contains(text(), "Yes, we operate under DGCA guidelines")]'

# Click on the FAQ question to reveal the answer
try:
    faq_question_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, faq_question_xpath_2))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_question_2)
    time.sleep(1)
    faq_question_2.click()
    print("Clicked FAQ: Is drone delivery safe and approved by Indian aviation authorities?")
    time.sleep(2)

    # Extract and print the answer
    faq_answer_2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, faq_answer_xpath_2))
    )
    print("Answer:")
    print(faq_answer_2.text)

except Exception as e:
    print("Failed to process the safety FAQ:", e)

# faq_spans = driver.find_elements(By.XPATH, '//span[text()="How is drone delivery different from traditional logistics services?"]')
# for span in faq_spans:
#     print(repr(span.text))

# Prtint the page source after clicking FAQ 3
# with open("page_after_faq3.html", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)


# # // Extracting all FAQ texts
# faq_spans = driver.find_elements(By.XPATH, '//span[contains(@class, "MuiTypography-root")]')
# print("FAQ Texts Found:")
# for i, span in enumerate(faq_spans):
#     print(f"{i+1}. {repr(span.text)}")


# // About Us Page
contact_us_button = driver.find_element(By.XPATH, "//a[text()='About Us']")
contact_us_button.click()
print("Contact Us button clicked.")
time.sleep(3)
# # Dilevery with Us Toady on the Home Page
# wait = WebDriverWait(driver, 10)
# delivery_today = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='delivery-text']")))
# delivery_today.click()
# time.sleep(5)
# # print(driver.page_source)  // Print the page source to verify navigation
# print(" Delivery with Us Today clicked.")

# # Delivery with us contct page
# wait = WebDriverWait(driver, 10)
# contact_us = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id ='«r0»']")))
# contact_us.send_keys("Atul")
# print(" Contact Us field filled with 'Atul'.")
# time.sleep(5)

# # Last Name Field
# last_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id ='«r1»']")))
# last_name.send_keys("Tiwari")
# print(" Last Name field filled with 'Tiwari'.")
# time.sleep(2)

# # Email Field
# email = driver.find_element(By.XPATH, "//input[@id ='«r2»']")
# email.send_keys("atul.tiwari@skyeair.tech")
# print(" Email field filled with 'atul.tiwari@skyeair.tech'.")
# time.sleep(2)

# # / mobile Number Field
# mobile_number = driver.find_element(By.XPATH, "//input[@id ='«r3»']")
# mobile_number.send_keys("1234567890")
# print(" Mobile Number field filled with '1234567890'.")
# time.sleep(2)

# # Message Field
# message = driver.find_element(By.NAME, "Message")
# message.send_keys("I want to schedule a flight for my Pacakge.")
# print("Message field filled with 'I want to schedule a flight for my Package.'.")  
# time.sleep(2)

# # Submit Button
# submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")  
# submit_button.click()
# print("Submit button clicked.")
# time.sleep(5)

# # close the Popup
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
#     close_popup.click()
#     print("Popup closed successfully.")
# except Exception as e:
#     print("No popup found or failed to close:", e)




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



# read_more_articles = driver.find_element(By.XPATH, "(//button[contains(@class, 'read-more-btn')])[1]")
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", read_more_articles)
# time.sleep(1)
# driver.execute_script("arguments[0].click();", read_more_articles)
# print("FAQ button clicked.")
# time.sleep(3)

# # read_more_articles_2 = driver.find_element(By.XPATH, "(//button[contains(@class, 'read-more-btn')])[2]")
# # read_more_articles_2.click()
# # print("Read More Articles button clicked.")
# # time.sleep(3)



# driver.get("https://www.skyeair.tech/about")  # Replace with your site

# Store parent window
parent_window = driver.current_window_handle

# Wait until all buttons are present
read_more_buttons = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'read-more-btn')]"))
)

# Get XPaths or indexes since list gets stale after tab switch
button_xpaths = [f"(//button[contains(@class, 'read-more-btn')])[{i+1}]" for i in range(len(read_more_buttons))]

# Loop through each button
for xpath in button_xpaths:
    # Scroll and click using JS (to avoid hidden issues)
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", button)

    # Wait for new window to appear
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    all_windows = driver.window_handles

    # Switch to new window
    for handle in all_windows:
        if handle != parent_window:
            driver.switch_to.window(handle)
            break

    print("Switched to new window:", driver.title)
    time.sleep(2)  # Optional: do something

    # Close child window and return to parent
    driver.close()
    driver.switch_to.window(parent_window)
    print("Returned to parent window\n")

# Done
print("All links processed successfully.")
time.sleep(5)

# # //clck on Gallery
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "swiper"))
# )

# # Try to click the next arrow
# for i in range(3):  # Click 3 times
#     try:
#         next_arrow = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Next")]'))
#         )
#         next_arrow.click()
#         time.sleep(1.5)
#     except Exception as e:
#         print(f"Error on iteration {i+1}: {e}")

        
# time.sleep(3)  # Wait for the last click to take effect

# Media & Partners 
media_partners = driver.find_element(By.XPATH, "//a[text()='Media & Partners']")
media_partners.click()      
print("Media & Partners button clicked.")
time.sleep(3)   

# Scroll to the bottom of the page to ensure all elements are loaded
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

time.sleep(3)  # Wait for the scroll to complete

# Contact Us Page

contact_us_button = driver.find_element(By.XPATH, "//a[text()='Contact Us']")
contact_us_button.click()       
print("Contact Us button clicked.")
time.sleep(3)

# contact Page  Fome on Page
# contact_us = driver.find_element(By.XPATH, "//input[@id ='«r0»']")
# contact_us.send_keys("Atul")
# print("Contact Us field filled with 'Atul'.")
# time.sleep(2)       
# # Last Name Field   
# last_name = driver.find_element(By.XPATH, "//input[@id ='«r1»']")
# last_name.send_keys("Tiwari")
# print("Last Name field filled with 'Tiwari'.")
# time.sleep(2)
# # Email Field
# email = driver.find_element(By.XPATH, "//input[@id ='«r2»']")
# email.send_keys("atul.tiwari@skyeair.tech")
# print("Email field filled with")
# # Phone Number Field
# phone_number = driver.find_element(By.XPATH, "//input[@id ='«r3»']")
# phone_number.send_keys("1234567890")
# print("Phone Number field filled with '1234567890'.")   
# time.sleep(2)
# # Message Field
# message = driver.find_element(By.NAME, "Message")
# message.send_keys("Hello Skye Air.")
# print("Message field filled with 'Hello Skye Air.'")
# time.sleep(2)
# # Submit Button
# submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
# submit_button.click()       
# print("Submit button clicked.")
# time.sleep(5)

# # close the Popup
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
#     close_popup.click()
#     print("Popup closed successfully.")
# except Exception as e:
#     print("No popup found or failed to close:", e)

# time.sleep(3)


# return to home page

wait = WebDriverWait(driver, 10)
return_home = driver.find_element(By.XPATH, "//img[@class='header-logo']")
# Scroll to the element before clicking
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", return_home)
time.sleep(1)
# Click the element
return_home.click()
print("Return Home button clicked.")
time.sleep(3)
# // Scroll to the bottom of the page to ensure all elements are loaded

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

# Scroll to the bottom of the page to ensure all elements are loaded
# time.sleep(3)  # Wait for the scroll to complete    

# # Find My Location Button
# find_my_location = driver.find_element(By.XPATH, "//span[text()='Find My Location']")
# # Scroll to the element before clicking
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", find_my_location)
# time.sleep(1)   
# # Click the element
# find_my_location.click()
# print("Find My Location button clicked.")   
# time.sleep(3)  # Wait for the action to complete    

# # Find our Location Button
# pin_code_input = driver.find_element(By.XPATH, "//input[@id='«r2»']")
# pin_code_input.send_keys("122001")  # Example pin code

# search_btn = driver.find_element(By.XPATH, "//button[@class='search-btn disabled']")
# search_btn.click()  # Click the search button
# print("Pin code '122001' entered.")

# time.sleep(2)
# # close the Popup
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
#     close_popup.click()
#     print("Popup closed successfully.")
# except Exception as e:
#     print("No popup found or failed to close:", e)


# // Solution Page 
solution_page = driver.find_element(By.XPATH, "//a[text()='Solutions']")
solution_page.click()
print("Solutions button clicked.")
time.sleep(3)

# // Request a Demo Button
request_demo_button = driver.find_element(By.XPATH, "(//button[text()='Request a Demo'])[1]")
# Scroll to the element before clicking
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", request_demo_button)
time.sleep(1)   
# Click the element
request_demo_button.click()
print("Request a Demo button clicked.")
time.sleep(3) 

# # // Request a Demo Form
# contact_us = driver.find_element(By.XPATH, "//input[@id ='«r0»']")
# contact_us.send_keys("Atul")
# print("Contact Us field filled with 'Atul'.")
# time.sleep(2)
# # Last Name Field 
# last_name = driver.find_element(By.XPATH, "//input[@id ='«r1»']")
# last_name.send_keys("Tiwari")
# print("Last Name field filled with 'Tiwari'.")
# time.sleep(2)

# #  Organization Field
# organization = driver.find_element(By.XPATH, "//input[@name ='Company']")
# organization.send_keys("Skye Air")
# print("Organization field filled with 'Skye Air'.")
# time.sleep(1)

# ## Click to open the Orginazation Role Dropdown
# Select_Dropdwon = driver.find_element(By.ID, "mui-component-select-Role")
# Select_Dropdwon.click()
# print("Role dropdown opened.")
# wait = WebDriverWait(driver, 10)
# # Select the option "Project Manager" from the dropdown
# wait = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Project Manager')]"))
# ).click()
# print("Project Manager selected")
# time.sleep(2)

# # Email Field
# email = driver.find_element(By.XPATH, "//input[@name ='Email']") 
# email.send_keys("atul.tiwari@skyeair.tech")
# print("Email field filled with 'atul.tiwari@skyeair.tech'")

# # Phone Number Field
# phone_number = driver.find_element(By.XPATH, "//input[@name ='Phone']")
# phone_number.send_keys("1234567890")
# print("Phone Number field filled with '1234567890'.")
# time.sleep(2)
# # Message Field
# message = driver.find_element(By.NAME, "Message")
# message.send_keys("Hello Skye Air.")
# print("Message field filled with 'Hello Skye Air.'")
# time.sleep(2)
# # Submit Button
# submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
# time.sleep(1)  # allow scroll animation to finish
# submit_button.click()
# print("Submit button clicked.")
# time.sleep(5)
# # close the Popup
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[@class='close-btn']")
#     close_popup.click()
#     print("Popup closed successfully.")
# except Exception as e:    
#     print("No popup found or failed to close:", e)    
# # back to the Solutions Page
# driver.back()

driver.back()  # Go back to the previous page (Solutions Page)
# Wait for the page to load
time.sleep(5)

driver.execute_script("window.scrollTo(0, 0);")  # Scroll to the top of the page


# # hover the Mouser on Modal
# hover_Modal_1 = driver.find_element(
#     By.XPATH,
#     "//div[contains(@class, 'slick-slide') and contains(@class, 'slick-active') and contains(@class, 'slick-current')]//h6[contains(@class, 'text-left') and contains(@class, 'fw-bold')]"
# )
# # Perform the hover
# actions = ActionChains(driver)
# actions.move_to_element(hover_Modal_1).perform()
# time.sleep(5)  # Wait for the hover effect to take place

# Hover the mouse on each modal card and show card info
modal_cards = driver.find_elements(
    By.XPATH,
    "//div[contains(@class, 'slick-slide') and contains(@class, 'slick-active')]//h6[contains(@class, 'text-left') and contains(@class, 'fw-bold')]"
)
actions = ActionChains(driver)
for i, card in enumerate(modal_cards, start=1):
    try:
        actions.move_to_element(card).perform()
        print(f"Hovered over card {i}: {card.text}")
        time.sleep(2)  # Wait for hover effect
    except Exception as e:
        print(f"Could not hover over card {i}: {e}")

# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hover_Modal_2)
# Click the element after scrolling into view

# Hover and click on Media & Partners
media_partners = driver.find_element(By.XPATH, "//a[@href='https://www.facebook.com/OfficialSkyeAirMobility/']//img[@alt='Logo']")
actions.move_to_element(media_partners).click().perform()
print("Media & Partners button clicked after hover.")
time.sleep(3)
driver.back()  # Go back to the previous page (Solutions Page)

# Instagram 
instagram_page = driver.find_element(By.XPATH, "//a[@href='https://www.instagram.com/skyeairofficial/']//img[@alt='Logo']")
actions.move_to_element(instagram_page).click().perform()
print("Instagram button clicked after hover.")
time.sleep(3)
driver.back()  # Go back to the previous page (Solutions Page)

# Twitter
twitter_page = driver.find_element(By.XPATH, "//a[@href='https://x.com/air_skye']//img[@alt='Logo']")
actions.move_to_element(twitter_page).click().perform()
driver.back()  # Go back to the previous page (Solutions Page)
print("Twitter button clicked after hover.")
time.sleep(3)

# LinkedIn
linkedin_page = driver.find_element(By.XPATH, "//a[@href='https://in.linkedin.com/company/skyeairmobility']//img[@alt='Logo']")
actions.move_to_element(linkedin_page).click().perform()
print("LinkedIn button clicked after hover.")
time.sleep(3)
driver.back()  # Go back to the previous page (Solutions Page)


# Close the browser


driver.quit()  # Close the browser after completion
print("Browser closed.")