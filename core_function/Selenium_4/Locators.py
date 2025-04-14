# Locators for Selenium 4
# 1. ID   2. Name  3. ClassName  4. TagName  5. LinkText  6. PartialLinkText
# 7. CSSSelector  8. XPath    9. DOM  10. JavaScript
# 11. By method (जैसे "name", "id", "xpath" आदि)
# 12. Value (जैसे "username", "email" आदि)     
# 13. Actions: Click  DoubleClick  RightClick  DragAndDrop  SendKeys
# 14. MoveToElement  ContextClick  ActionChains  KeyDown  KeyUp

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)
