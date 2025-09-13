

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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

webdriver = webdriver.Chrome() # Step 1: Open Chrome browser
webdriver.maximize_window() # Step 2: Maximize the browser window
webdriver.get("https://www.saucedemo.com/") # Step 3: Navigate to the URL
# webdriver.implicitly_wait(10) # Step 4: Wait for elements to load
time.sleep(2) # Wait for 2 seconds to see the page load

# Enter your username
username = webdriver.find_element(By.XPATH, value="//input[@id='user-name']")
username.send_keys("standard_user")
time.sleep(2) # Wait for 2 seconds to see the page loadcd

# Enter your password
password = webdriver.find_element(By.XPATH, value = "//input[@id='password']")
password.send_keys("secret_sauce")
time.sleep(2) # Wait for 2 seconds to see the page load

#  Login Button

login_button = webdriver.find_element(By.XPATH, value="//input[@name='login-button']")
login_button.click()
time.sleep(2) # Wait for 2 seconds to see the page load

#             #  after login add to cart button ( using contains method)
# # contains method is used to find an element whose attribute contains a specific value.
# # Example: //button[contains(@class, 'btn_primary') and contains(text(), 'Add to cart')]
# # add_to_cart_button = webdriver.find_element(By.XPATH, value="//button[contains(@name,'add-to-cart-sauce-labs-backpack')]") 
# # add_to_cart_button.click()

# wait = WebDriverWait(webdriver, 10)
# add_to_cart_button = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "//button[contains(@name,'add-to-cart-sauce-labs-backpack')]")
# ))
# add_to_cart_button.click()

# # Remove from cart
# remove_button = wait.until(EC.presence_of_element_located(
#     (By.XPATH, "//button[contains(@name,'remove-sauce-labs-backpack')]")
# ))
# remove_button.click()
# time.sleep(3)

# # Text method is used to find an element whose text matches a specific value.
# # Example: //button[text()='Remove']

# add_text = webdriver.find_element(By.XPATH, value="//div[text()='Sauce Labs Backpack']")
# add_text.click()
# # print(add_text.text) # Print the text of the element

# Finding duplicate vlaue using x path
# username_duplicate = webdriver.find_element(By.XPATH,value="//input[@id='user-name' and @name='user-name']")
# username_duplicate.send_keys("standard_user")
# time.sleep(2) # Wait for 2 seconds to see the page load
# print("Name is entered successfully")


# Link Text

product_link = webdriver.find_element(By.LINK_TEXT, value="Sauce Labs Backpack")
product_link.click()

time.sleep(15) # Wait for 2 seconds to see the page load

webdriver.quit() # Step 5: Close the browser

