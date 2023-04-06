import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def browser():
    # Use Chrome browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_add_to_do_item(browser):
    # Open the application
    browser.get("https://todoapp.com")

    # Add a new to-do item
    add_button = browser.find_element_by_xpath("//button[text()='Add New']")
    add_button.click()

    title_field = browser.find_element_by_name("title")
    title_field.send_keys("Buy groceries")

    description_field = browser.find_element_by_name("description")
    description_field.send_keys("Milk, eggs, bread")

    save_button = browser.find_element_by_xpath("//button[text()='Save']")
    save_button.click
