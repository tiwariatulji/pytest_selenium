# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

# def setup_browser(browser_name):
#     if browser_name.lower() == 'chrome':
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#     elif browser_name.lower() == 'firefox':
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     else:
#         raise ValueError("Unsupported browser")
#     driver.maximize_window()
#     return driver

# -------  New version 4.10 ----------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService  # नया इम्पोर्ट
from selenium.webdriver.firefox.service import Service as FirefoxService  # नया इम्पोर्ट
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def setup_browser(browser_name):
    if browser_name.lower() == 'chrome':
        # Chrome के लिए नया सिंटैक्स
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.lower() == 'firefox':
        # Firefox के लिए नया सिंटैक्स
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    return driver