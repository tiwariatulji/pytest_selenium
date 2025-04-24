

# # there are two types of XPath:
# # 1. Absolute XPath: This is the full path to the element starting from the root of the document.
# # It begins with a single slash (/) and follows the hierarchy of elements in the HTML document. 
# # Example: /html/body/div[1]/div[2]/div[1]/input

# # 2. Relative XPath: This is a more flexible way to locate elements.
# # It starts with a double slash (//) and can be used to find elements anywhere in the document.
# # It allows you to use various attributes and functions to identify elements.
# # Example: //input[@id='username'] or //input[contains(@class, 'login')] or //button[text()='Login']
# # Example of Absolute XPath:

# # //tagname[@attribute='value']
# # Example of Relative XPath:

# <html>
#   <body>
#     <div>
#       <h1>Welcome to My Website</h1>
#       <p id="intro">This is a sample paragraph.</p>
#       <button>Click Me</button>
#     </div>
#   </body>
# </html>
# # Absolute XPath: /html/body/div/h1
# #Relative XPath:
# # //p[@id='intro'] (This will find the <p> element with id 'intro'.)
# # //button[text()='Click Me'] (This will find the <button> element with the text 'Click Me'.)
# # Relative XPath: //h1 (This will find the <h1> element regardless of its position in the document.)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver = webdriver.Chrome() # Step 1: Open Chrome browser
webdriver.maximize_window() # Step 2: Maximize the browser window
webdriver.get("https://www.saucedemo.com/") # Step 3: Navigate to the URL
# webdriver.implicitly_wait(10) # Step 4: Wait for elements to load
time.sleep(2) # Wait for 2 seconds to see the page load

# Enter your username
username = webdriver.find_element(By.XPATH, value="//input[@id='user-name']")
username.send_keys("standard_user")
time.sleep(2) # Wait for 2 seconds to see the page load

# Enter your password
password = webdriver.find_element(By.XPATH, value = "//input[@id='password']")
password.send_keys("secret_sauce")
time.sleep(2) # Wait for 2 seconds to see the page load