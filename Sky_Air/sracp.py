
import requests
import json

TOKEN = ""

url = f"https://api.diffbot.com/v3/analyze?token={TOKEN}"

headers = {}

params = {
  "url": "https://www.healthians.com/"
}

response = requests.request("GET", url, params=params, headers=headers)

print(response.text)



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# --- POM Classes ---

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)

    def click_element(self, element):
        self.scroll_to_element(element)
        element.click()
        time.sleep(1)

    def scroll_to_bottom(self):
        scroll_pause_time = 1
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return window.pageYOffset + window.innerHeight")
            if new_height >= last_height:
                break

class HomePage(BasePage):
    DELIVERY_TODAY_XPATH = "//span[@class='delivery-text']"
    FAQ1_XPATH = '//span[text()="What is Skye Air and how does drone delivery work?"]'
    FAQ2_XPATH = '//span[text()="Which areas or cities in India does Skye Air currently operate in?"]'
    FAQ3_XPATH = '//span[text()="What types of goods can be delivered using Skye Air drones?"]'
    FAQ4_XPATH = '//span[text()="How is drone delivery different from traditional logistics services?"]'
    FAQ4_ANSWER_XPATH = '//p[contains(text(), "Drone delivery is faster")]'
    FAQ_SAFE_XPATH = '//span[contains(text(), "Is drone delivery safe and approved by Indian aviation authorities?")]'
    FAQ_SAFE_ANSWER_XPATH = '//p[contains(text(), "Yes, we operate under DGCA guidelines")]'
    ABOUT_US_XPATH = "//a[text()='About Us']"
    MEDIA_PARTNERS_XPATH = "//a[text()='Media & Partners']"
    HEADER_LOGO_XPATH = "//img[@class='header-logo']"
    SOLUTIONS_XPATH = "//a[text()='Solutions']"
    REQUEST_DEMO_BTN_XPATH = "(//button[text()='Request a Demo'])[1]"
    READ_MORE_BTN_XPATH = "(//button[contains(@class, 'read-more-btn')])[1]"

    def click_delivery_today(self):
        delivery_today = self.wait.until(EC.presence_of_element_located((By.XPATH, self.DELIVERY_TODAY_XPATH)))
        self.click_element(delivery_today)
        print("Delivery with Us Today clicked.")

    def click_faqs(self):
        faq1 = self.driver.find_element(By.XPATH, self.FAQ1_XPATH)
        self.click_element(faq1)
        print("FAQ button clicked.")

        faq2 = self.driver.find_element(By.XPATH, self.FAQ2_XPATH)
        faq2.click()
        print("FAQ 2 button clicked.")

        faq3 = self.driver.find_element(By.XPATH, self.FAQ3_XPATH)
        faq3.click()
        print("FAQ 3 button clicked.")
        time.sleep(3)

        # FAQ 4
        try:
            faq4 = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.FAQ4_XPATH)))
            self.scroll_to_element(faq4)
            faq4.click()
            print("FAQ Button 4 clicked.")
            time.sleep(2)
        except Exception as e:
            print("Failed to click FAQ 4:", e)

        try:
            faq4_answer = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.FAQ4_ANSWER_XPATH)))
            print("FAQ 4 Answer:")
            print(faq4_answer.text)
        except Exception as e:
            print("Could not find FAQ 4 Answer:", e)

        # Safety FAQ
        try:
            faq_safe = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.FAQ_SAFE_XPATH)))
            self.scroll_to_element(faq_safe)
            faq_safe.click()
            print("Clicked FAQ: Is drone delivery safe and approved by Indian aviation authorities?")
            time.sleep(2)
            faq_safe_answer = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.FAQ_SAFE_ANSWER_XPATH)))
            print("Answer:")
            print(faq_safe_answer.text)
        except Exception as e:
            print("Failed to process the safety FAQ:", e)

    def click_about_us(self):
        about_us = self.driver.find_element(By.XPATH, self.ABOUT_US_XPATH)
        self.click_element(about_us)
        print("About Us button clicked.")

    def click_media_partners(self):
        media_partners = self.driver.find_element(By.XPATH, self.MEDIA_PARTNERS_XPATH)
        self.click_element(media_partners)
        print("Media & Partners button clicked.")

    def click_return_home(self):
        return_home = self.driver.find_element(By.XPATH, self.HEADER_LOGO_XPATH)
        self.click_element(return_home)
        print("Return Home button clicked.")

    def click_solutions(self):
        solutions = self.driver.find_element(By.XPATH, self.SOLUTIONS_XPATH)
        self.click_element(solutions)
        print("Solutions button clicked.")

    def click_request_demo(self):
        request_demo = self.driver.find_element(By.XPATH, self.REQUEST_DEMO_BTN_XPATH)
        self.click_element(request_demo)
        print("Request a Demo button clicked.")

    def click_read_more_articles(self):
        read_more = self.driver.find_element(By.XPATH, self.READ_MORE_BTN_XPATH)
        self.click_element(read_more)
        print("Read More Articles button clicked.")

    def process_all_read_more_links(self):
        parent_window = self.driver.current_window_handle
        read_more_buttons = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class, 'read-more-btn')]"))
        )
        button_xpaths = [f"(//button[contains(@class, 'read-more-btn')])[{i+1}]" for i in range(len(read_more_buttons))]
        for xpath in button_xpaths:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.scroll_to_element(button)
            button.click()
            WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
            all_windows = self.driver.window_handles
            for handle in all_windows:
                if handle != parent_window:
                    self.driver.switch_to.window(handle)
                    break
            print("Switched to new window:", self.driver.title)
            time.sleep(2)
            self.driver.close()
            self.driver.switch_to.window(parent_window)
            print("Returned to parent window\n")
        print("All links processed successfully.")

class RequestDemoFormPage(BasePage):
    CONTACT_US_XPATH = "//input[@id ='«r0»']"
    LAST_NAME_XPATH = "//input[@id ='«r1»']"
    ORGANIZATION_NAME = "Company"
    PHONE_NUMBER_XPATH = "//input[@name='Name']"
    EMAIL_XPATH = "//input[@id ='«r2»']"
    MESSAGE_NAME = "Message"
    SUBMIT_BTN_XPATH = "//button[normalize-space()='Submit']"
    CLOSE_POPUP_XPATH = "//button[@class='close-btn']"

    def fill_form(self, first_name, last_name, organization, phone, message):
        self.driver.find_element(By.XPATH, self.CONTACT_US_XPATH).send_keys(first_name)
        print(f"Contact Us field filled with '{first_name}'.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.LAST_NAME_XPATH).send_keys(last_name)
        print(f"Last Name field filled with '{last_name}'.")
        time.sleep(2)
        self.driver.find_element(By.NAME, self.ORGANIZATION_NAME).send_keys(organization)
        print(f"Organization field filled with '{organization}'.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.PHONE_NUMBER_XPATH).send_keys(phone)
        print(f"Phone Number field filled with '{phone}'.")
        time.sleep(2)
        self.driver.find_element(By.NAME, self.MESSAGE_NAME).send_keys(message)
        print(f"Message field filled with '{message}'.")
        time.sleep(2)

    def submit_form(self):
        self.driver.find_element(By.XPATH, self.SUBMIT_BTN_XPATH).click()
        print("Submit button clicked.")
        time.sleep(5)

    def close_popup(self):
        try:
            close_popup = self.driver.find_element(By.XPATH, self.CLOSE_POPUP_XPATH)
            close_popup.click()
            print("Popup closed successfully.")
        except Exception as e:
            print("No popup found or failed to close:", e)

# --- Test/Runner Code ---

def main():
    # Setup Chrome with options
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 1}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://uat.skyeair.tech/home")
    print("Page Title:", driver.title)
    assert "Sky" in driver.title or "Air" in driver.title
    time.sleep(10)
    print("Page loaded successfully.")

    home_page = HomePage(driver)

    # Home Page actions
    home_page.click_delivery_today()
    home_page.click_faqs()
    home_page.click_about_us()
    home_page.scroll_to_bottom()
    home_page.click_read_more_articles()
    home_page.process_all_read_more_links()
    home_page.click_media_partners()
    home_page.scroll_to_bottom()
    home_page.click_return_home()
    home_page.scroll_to_bottom()
    home_page.click_solutions()
    home_page.click_request_demo()

    # Request a Demo Form actions
    request_demo_form = RequestDemoFormPage(driver)
    request_demo_form.fill_form(
        first_name="Atul",
        last_name="Tiwari",
        organization="Skye Air",
        phone="1234567890",
        message="Hello Skye Air."
    )
    request_demo_form.submit_form()
    request_demo_form.close_popup()
    driver.back()

   
   
    driver.quit()
    print("Browser closed.")

if __name__ == "__main__":
    main()
      


      