import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from utilities.browser import setup_browser


@pytest.fixture(scope="session")
def test_config():
    """Test configuration fixture"""
    return {
        "base_url": "https://uat.skyeairops.tech/operator/cod",
        "username": "atul.tiwari@skyeair.tech",
        "password": "Atul@123",
        "timeout": 20,
        "screenshots_dir": "pytest_selenium/Sky_Air/screenshots",
        "reports_dir": "pytest_selenium/Sky_Air/reports"
    }


@pytest.fixture(scope="function")
def browser():
    """Browser fixture with Chrome options"""
    driver = setup_browser('chrome')
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def chrome_driver_with_options():
    """Chrome driver with specific options for SkyeAir testing"""
    chrome_options = Options()
    prefs = {
        "profile.default_content_setting_values.notifications": 1,  # Allow notifications
        "profile.default_content_settings.popups": 0,  # Block popups
        "profile.managed_default_content_settings.images": 2  # Don't load images for faster execution
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait_driver(chrome_driver_with_options):
    """WebDriverWait fixture"""
    return WebDriverWait(chrome_driver_with_options, 20)


@pytest.fixture(autouse=True)
def setup_test_directories():
    """Automatically create test directories"""
    directories = [
        "pytest_selenium/Sky_Air/screenshots",
        "pytest_selenium/Sky_Air/reports"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


@pytest.fixture(scope="function")
def screenshot_helper(chrome_driver_with_options):
    """Screenshot helper fixture"""
    def take_screenshot(step_name, status="info"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{status}_{step_name}_{timestamp}.png"
        filepath = os.path.join("pytest_selenium/Sky_Air/screenshots", filename)
        chrome_driver_with_options.save_screenshot(filepath)
        print(f"Screenshot saved: {filename}")
        return filepath
    
    return take_screenshot


def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "skyewalker: mark test as skyewalker related"
    )
    config.addinivalue_line(
        "markers", "attendance: mark test as attendance related"
    )


def pytest_html_report_title(report):
    """Customize HTML report title"""
    report.title = "SkyeAir Automation Test Report"


def pytest_html_results_summary(prefix, summary, postfix):
    """Customize HTML report summary"""
    prefix.extend([
        "<h2>SkyeAir Test Execution Summary</h2>",
        f"<p>Test execution completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>"
    ])


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get the driver from the test instance if available
        if hasattr(item.instance, 'driver'):
            driver = item.instance.driver
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"failure_{item.name}_{timestamp}.png"
            screenshot_path = os.path.join("pytest_selenium/Sky_Air/screenshots", screenshot_name)
            
            try:
                driver.save_screenshot(screenshot_path)
                print(f"Failure screenshot saved: {screenshot_name}")
                
                # Add screenshot to HTML report
                if hasattr(report, 'extra'):
                    report.extra = getattr(report, 'extra', [])
                    report.extra.append({
                        'name': 'Screenshot',
                        'content': screenshot_path,
                        'content_type': 'image'
                    })
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")


# Custom assertion helpers
class TestAssertions:
    """Custom assertion helpers for SkyeAir tests"""
    
    @staticmethod
    def assert_element_present(driver, locator, timeout=10):
        """Assert that element is present"""
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(driver, timeout)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except:
            raise AssertionError(f"Element not found: {locator}")
    
    @staticmethod
    def assert_element_clickable(driver, locator, timeout=10):
        """Assert that element is clickable"""
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(driver, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            return element
        except:
            raise AssertionError(f"Element not clickable: {locator}")
    
    @staticmethod
    def assert_text_present(driver, text, timeout=10):
        """Assert that text is present on page"""
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        wait = WebDriverWait(driver, timeout)
        try:
            wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text))
            return True
        except:
            raise AssertionError(f"Text not found on page: {text}")


@pytest.fixture
def assertions():
    """Fixture to provide custom assertions"""
    return TestAssertions()