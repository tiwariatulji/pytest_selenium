import pytest
from selenium import webdriver
from utilities.browser import setup_browser

@pytest.fixture(scope="function")
def browser():
    driver = setup_browser('chrome')
    yield driver
    driver.quit()