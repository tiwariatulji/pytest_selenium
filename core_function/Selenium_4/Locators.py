# Locators for Selenium 4


# 1. ID   2. Name  3. ClassName  4. TagName  5. LinkText  6. PartialLinkText
# 7. CSSSelector  8. XPath    9. DOM  10. JavaScript
# Selenium की find_element() को दो पैरामीटर चाहिए होते हैं:
# 11. By method (जैसे "name", "id", "xpath" आदि)
# 12. Value (जैसे "username", "email" आदि)     
# 13. Actions: Click  DoubleClick  RightClick  DragAndDrop  SendKeys
# 14. MoveToElement  ContextClick  ActionChains  KeyDown  KeyUp

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Locate your username web element
username = driver.find_element(By.ID, value="user-name")
# Enter your username
username.send_keys("standard_user")
time.sleep(2)
# Locate your password web element
password = driver.find_element(By.ID, value="password")
password.send_keys("secret_sauce")
time.sleep(2)


# // Find Product link for By.LINK_TEXT
product_link



driver.quit()