# Skye Air Website Test Automation

This project implements a Page Object Model (POM) framework for testing the Skye Air website.

## Project Structure

```
pytest_selenium/
├── pages/
│   ├── base_page.py                # Base page with common methods
│   ├── home_page.py                # Home page object
│   ├── about_us_page.py            # About Us page object
│   ├── media_partners_page.py      # Media & Partners page object
│   ├── contact_us_page.py          # Contact Us page object
│   ├── solutions_page.py           # Solutions page object
│   └── components/                  # Reusable components across pages
│       └── header_component.py      # Header navigation component
├── tests/
│   ├── test_home_page.py           # Tests for home page
│   ├── test_about_us_page.py       # Tests for about us page
│   ├── test_media_partners_page.py # Tests for media partners page
│   ├── test_contact_us_page.py     # Tests for contact us page
│   ├── test_solutions_page.py      # Tests for solutions page
│   ├── test_skye_air.py            # Full site navigation test
│   └── test_skye_air_web_pom.py    # Refactored original script
├── utilities/
│   ├── browser.py                  # Browser setup and configuration
│   └── config.py                   # Configuration settings
└── conftest.py                     # Pytest fixtures
```

## Usage

### Running Tests

To run all tests:

```bash
python -m pytest pytest_selenium/tests/
```

To run a specific test file:

```bash
python -m pytest pytest_selenium/tests/test_home_page.py
```

To run the refactored original script:

```bash
python -m pytest_selenium.tests.test_skye_air_web_pom
```

### Creating New Tests

To create a new test using the POM framework:

1. Import the required page objects:

```python
from pages.home_page import HomePage
from pages.about_us_page import AboutUsPage
# Import other page objects as needed
```

2. Initialize the page objects with the WebDriver instance:

```python
def test_example(browser):
    home_page = HomePage(browser)
    about_us_page = AboutUsPage(browser)
    # Initialize other page objects as needed
```

3. Use the page objects to interact with the website:

```python
def test_example(browser):
    home_page = HomePage(browser)
    home_page.load()
    
    # Perform actions on the home page
    home_page.click_faq_1()
    
    # Navigate to another page
    home_page.header.navigate_to_about_us()
    
    # Initialize the new page object
    about_us_page = AboutUsPage(browser)
    
    # Perform actions on the about us page
    about_us_page.scroll_to_bottom()
```

## Page Objects

### BasePage

The BasePage class provides common methods used across all page objects:

- Finding elements
- Clicking elements
- Sending keys to elements
- Scrolling
- Waiting for elements
- Handling windows/tabs
- And more

### Page-Specific Objects

Each page object represents a specific page on the website and provides methods for interacting with that page:

- HomePage: Methods for interacting with the home page, including FAQs
- AboutUsPage: Methods for interacting with the About Us page
- MediaPartnersPage: Methods for interacting with the Media & Partners page
- ContactUsPage: Methods for interacting with the Contact Us page
- SolutionsPage: Methods for interacting with the Solutions page

### Components

Components represent reusable parts of the website that appear on multiple pages:

- HeaderComponent: Methods for interacting with the header navigation

## Benefits of POM

1. **Maintainability**: Changes to the UI only require updates in one place (the page object), not in multiple test files.

2. **Reusability**: Page objects can be reused across multiple test cases, reducing code duplication.

3. **Readability**: Tests are more readable and focused on the business logic rather than the implementation details.

4. **Scalability**: New tests can be added easily by reusing existing page objects.

5. **Stability**: Tests are more stable as they use robust element location strategies and wait mechanisms.

## Verification Process

To ensure the implementation works correctly:

1. Run the refactored script and compare its behavior with the original script
2. Run individual test files to verify specific functionality
3. Run the full test suite to ensure all tests pass
4. Review the code for proper documentation and error handling