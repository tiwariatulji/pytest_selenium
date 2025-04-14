
# def fun2(): 
#     print("Hello")
#     return "hello"
    
# if __name__ == '__main__':
#     fun2()

   
# from selenium import webdriver  // this is old version of below 4.0
# driver = webdriver.Chrome (executable_path="E:\\chromedriver-win32\\chromedriver.exe")
# driver.get("https://www.Healthians.com")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("E:\\chromedriver-win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

# Locators:
# 1. ID     2. Name  3. ClassName  4. TagName  5. LinkText  6. PartialLinkText
# 7. CSSSelector  8. XPath
# 9. DOM  10. JavaScript
#  Actions:     
# 1. Click  2. DoubleClick  3. RightClick  4. DragAndDrop  5. SendKeys
# 6. MoveToElement  7. ContextClick  8. ActionChains  9. KeyDown  10. KeyUp
# driver.find_element("name", "username").send_keys("Har Har Mahadev")
# यहाँ "name" तो बताया गया है, लेकिन किस एलिमेंट का name attribute है, वो "value" देना जरूरी होता है। Selenium की find_element() को दो पैरामीटर चाहिए होते हैं:

# By method (जैसे "name", "id", "xpath" आदि)

# Value (जैसे "username", "email" आदि)

driver.find_element("id", "name").send_keys("Har Har Mahadev")