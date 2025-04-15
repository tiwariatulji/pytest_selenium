


# import webdriver module from selenium package
# from selenium import webdriver

# # instantiate webdriver and launch crome browser
# driver = webdriver.Chrome()

# # open the URL in the browser
# driver.get("https://www.Healthians.com")

# # print the title of the page
# print(driver.title)

# # close the browser window
# driver.quit()

# -------------- # Navigation Scenario

# Step 1: Open Chrome browser
# Step 2: Navigate to Google
# Step 3: Navigate to YouTube
# Step 4: go back to Google.
# Step 5: go forward to YouTube.
# Step 6: refresh the current page (YouTube).
# Step 7: Close the browser

from selenium import webdriver 
import time

driver = webdriver.Chrome() # Step 1: Open Chrome browser
driver.get("https://www.google.com")
time.sleep(5) # Wait for 10 seconds to see the page load

 # Step 2: Navigate to Google
driver.get("https://www.youtube.com") # Step 3: Navigate to YouTube
time.sleep(5) # Wait for 10 seconds to see the page load

# go back to Google.
driver.back()
time.sleep(2) # Wait for 2 seconds to see the page load

# go froward to YouTube.
driver.forward()
time.sleep(2) # Wait for 2 seconds to see the page load

# refresh the current page 
driver.refresh() 

# close the browser window
driver.quit() # Step 7: Close the browser