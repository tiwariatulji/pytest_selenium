def test_example_search(browser):
    browser.get("https://www.healthians.com")
    assert "Healthians" in browser.title