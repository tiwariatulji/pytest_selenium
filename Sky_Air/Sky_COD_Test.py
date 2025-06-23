import pytest
import time
from unittest.mock import Mock, patch, MagicMock
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, 
    TimeoutException, 
    WebDriverException
)


class TestCODFunctionality:
    """Test suite for COD (Cash on Delivery) functionality"""
    
    @pytest.fixture
    def mock_driver(self):
        """Create a mock WebDriver for testing"""
        driver = Mock(spec=webdriver.Chrome)
        return driver
    
    @pytest.fixture
    def mock_element(self):
        """Create a mock WebElement"""
        element = Mock()
        element.text = "COD"
        element.is_displayed.return_value = True
        element.is_enabled.return_value = True
        return element
    
    def test_find_cod_element_success(self, mock_driver, mock_element):
        """Test successful finding of COD element"""
        # Arrange
        mock_driver.find_element.return_value = mock_element
        
        # Act
        cod_element = mock_driver.find_element(By.XPATH, "//span[text()='COD']")
        
        # Assert
        mock_driver.find_element.assert_called_once_with(By.XPATH, "//span[text()='COD']")
        assert cod_element.text == "COD"
        assert cod_element.is_displayed()
    
    def test_find_cod_element_not_found(self, mock_driver):
        """Test handling when COD element is not found"""
        # Arrange
        mock_driver.find_element.side_effect = NoSuchElementException("Element not found")
        
        # Act & Assert
        with pytest.raises(NoSuchElementException):
            mock_driver.find_element(By.XPATH, "//span[text()='COD']")
    
    def test_find_cod_element_with_wait(self, mock_driver, mock_element):
        """Test finding COD element with explicit wait"""
        # Arrange
        mock_wait = Mock(spec=WebDriverWait)
        mock_wait.until.return_value = mock_element
        
        with patch('selenium.webdriver.support.wait.WebDriverWait', return_value=mock_wait):
            # Act
            wait = WebDriverWait(mock_driver, 10)
            cod_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='COD']")))
            
            # Assert
            assert cod_element == mock_element
            mock_wait.until.assert_called_once()
    
    def test_find_cod_element_timeout(self, mock_driver):
        """Test timeout when waiting for COD element"""
        # Arrange
        mock_wait = Mock(spec=WebDriverWait)
        mock_wait.until.side_effect = TimeoutException("Timeout waiting for element")
        
        with patch('selenium.webdriver.support.wait.WebDriverWait', return_value=mock_wait):
            # Act & Assert
            wait = WebDriverWait(mock_driver, 10)
            with pytest.raises(TimeoutException):
                wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='COD']")))
    
    def test_cod_element_click(self, mock_driver, mock_element):
        """Test clicking on COD element"""
        # Arrange
        mock_driver.find_element.return_value = mock_element
        
        # Act
        cod_element = mock_driver.find_element(By.XPATH, "//span[text()='COD']")
        cod_element.click()
        
        # Assert
        mock_element.click.assert_called_once()
    
    def test_cod_element_visibility(self, mock_driver, mock_element):
        """Test checking COD element visibility"""
        # Arrange
        mock_driver.find_element.return_value = mock_element
        
        # Act
        cod_element = mock_driver.find_element(By.XPATH, "//span[text()='COD']")
        is_visible = cod_element.is_displayed()
        
        # Assert
        assert is_visible
        mock_element.is_displayed.assert_called_once()
    
    def test_alternative_xpath_strategies(self, mock_driver, mock_element):
        """Test alternative XPath strategies for finding COD element"""
        xpath_strategies = [
            "//span[text()='COD']",
            "//span[contains(text(), 'COD')]",
            "//span[@class='payment-option'][text()='COD']",
            "//*[text()='COD']",
            "//span[normalize-space()='COD']"
        ]
        
        for xpath in xpath_strategies:
            # Arrange
            mock_driver.find_element.return_value = mock_element
            
            # Act
            element = mock_driver.find_element(By.XPATH, xpath)
            
            # Assert
            assert element == mock_element
    
    def test_cod_element_with_retry_mechanism(self, mock_driver, mock_element):
        """Test COD element finding with retry mechanism"""
        # Arrange
        mock_driver.find_element.side_effect = [
            NoSuchElementException("Not found"),
            NoSuchElementException("Not found"),
            mock_element  # Success on third try
        ]
        
        # Act
        max_retries = 3
        for attempt in range(max_retries):
            try:
                cod_element = mock_driver.find_element(By.XPATH, "//span[text()='COD']")
                break
            except NoSuchElementException:
                if attempt == max_retries - 1:
                    raise
                time.sleep(1)  # Wait before retry
        
        # Assert
        assert cod_element == mock_element
        assert mock_driver.find_element.call_count == 3


class TestCODPageInteractions:
    """Test suite for COD page interactions"""
    
    @pytest.fixture
    def mock_driver(self):
        driver = Mock(spec=webdriver.Chrome)
        return driver
    
    def test_page_load_before_cod_search(self, mock_driver):
        """Test that page loads before searching for COD element"""
        # Arrange
        mock_driver.current_url = "https://example.com/checkout"
        mock_driver.title = "Checkout Page"
        
        # Act & Assert
        assert "checkout" in mock_driver.current_url.lower()
        assert mock_driver.title == "Checkout Page"
    
    def test_cod_selection_workflow(self, mock_driver):
        """Test complete COD selection workflow"""
        # Arrange
        cod_element = Mock()
        confirm_button = Mock()
        mock_driver.find_element.side_effect = [cod_element, confirm_button]
        
        # Act
        cod_option = mock_driver.find_element(By.XPATH, "//span[text()='COD']")
        cod_option.click()
        
        confirm_btn = mock_driver.find_element(By.XPATH, "//button[text()='Confirm Order']")
        confirm_btn.click()
        
        # Assert
        cod_element.click.assert_called_once()
        confirm_button.click.assert_called_once()
    
    def test_cod_validation_message(self, mock_driver):
        """Test COD validation message appears"""
        # Arrange
        validation_element = Mock()
        validation_element.text = "Cash on Delivery selected"
        mock_driver.find_element.return_value = validation_element
        
        # Act
        message = mock_driver.find_element(By.XPATH, "//div[@class='validation-message']")
        
        # Assert
        assert "Cash on Delivery" in message.text


class TestCODErrorHandling:
    """Test suite for COD error handling scenarios"""
    
    @pytest.fixture
    def mock_driver(self):
        return Mock(spec=webdriver.Chrome)
    
    def test_webdriver_exception_handling(self, mock_driver):
        """Test handling of WebDriver exceptions"""
        # Arrange
        mock_driver.find_element.side_effect = WebDriverException("WebDriver error")
        
        # Act & Assert
        with pytest.raises(WebDriverException):
            mock_driver.find_element(By.XPATH, "//span[text()='COD']")
    
    def test_stale_element_reference(self, mock_driver):
        """Test handling of stale element reference"""
        from selenium.common.exceptions import StaleElementReferenceException
        
        # Arrange
        mock_element = Mock()
        mock_element.click.side_effect = StaleElementReferenceException("Element is stale")
        mock_driver.find_element.return_value = mock_element
        
        # Act & Assert
        cod_element = mock_driver.find_element(By.XPATH, "//span[text()='COD']")
        with pytest.raises(StaleElementReferenceException):
            cod_element.click()


# Helper function for robust element finding
def find_cod_element_robust(driver, timeout=10):
    """
    Robust function to find COD element with multiple strategies
    
    Args:
        driver: WebDriver instance
        timeout: Maximum time to wait for element
    
    Returns:
        WebElement: The COD element if found
    
    Raises:
        NoSuchElementException: If element not found after all strategies
    """
    strategies = [
        "//span[text()='COD']",
        "//span[contains(text(), 'COD')]",
        "//*[text()='COD']",
        "//span[normalize-space()='COD']",
        "//span[@title='Cash on Delivery']"
    ]
    
    wait = WebDriverWait(driver, timeout)
    
    for strategy in strategies:
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, strategy)))
            if element.is_displayed():
                return element
        except TimeoutException:
            continue
    
    raise NoSuchElementException("COD element not found with any strategy")


# Test the helper function
class TestCODHelperFunction:
    """Test the robust COD finding helper function"""
    
    def test_find_cod_element_robust_success(self):
        """Test successful finding with helper function"""
        # Arrange
        mock_driver = Mock()
        mock_element = Mock()
        mock_element.is_displayed.return_value = True
        
        with patch('selenium.webdriver.support.wait.WebDriverWait') as mock_wait_class:
            mock_wait = Mock()
            mock_wait.until.return_value = mock_element
            mock_wait_class.return_value = mock_wait
            
            # Act
            result = find_cod_element_robust(mock_driver)
            
            # Assert
            assert result == mock_element
    
    def test_find_cod_element_robust_failure(self):
        """Test failure with helper function"""
        # Arrange
        mock_driver = Mock()
        
        with patch('selenium.webdriver.support.wait.WebDriverWait') as mock_wait_class:
            mock_wait = Mock()
            mock_wait.until.side_effect = TimeoutException("Timeout")
            mock_wait_class.return_value = mock_wait
            
            # Act & Assert
            with pytest.raises(NoSuchElementException):
                find_cod_element_robust(mock_driver)


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])