from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture(scope="module")
def driver():
    # Setup: Initialize the WebDriver using the Service class
    driver = webdriver.Chrome()  # Use the Service instance
    yield driver  # This allows the test to use the driver
    driver.quit()  # Teardown: Close the browser after the test

def test_google_title(driver):
    # Open Google
    driver.get("https://www.google.com")

    # Get and print the title of the page
    print("Title of the page is:", driver.title)

    # Check if the title matches "Google"
    assert "Google" in driver.title, "Title does not match!"
