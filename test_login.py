import pytest
from selenium import webdriver
from Test_Automation.ActionPage.pages import (LoginPage, AddCustomerPage, NewCustomerPage, LogOutPage)


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def test_login(browser):
    login_page = LoginPage(browser)
    login_page.get("https://automationplayground.com/crm/login.html")
    login_page.enter_username("henryokolie@gamil.com")
    login_page.enter_password("Passw0rd@123")
    login_page.click_remember_button()
    login_page.click_login_button()


def test_add_customer_page(browser):
    add_customer_page = AddCustomerPage(browser)
    add_customer_page.click_add_customer_button()


def test_new_customer_page(browser):
    new_customer_page = NewCustomerPage(browser)
    new_customer_page.enter_email_address("john.doe@example.com")
    new_customer_page.enter_first_name("John")
    new_customer_page.enter_last_name("Doe")
    new_customer_page.enter_city("USA")
    new_customer_page.select_gender_button()
    new_customer_page.add_to_promoter()
    new_customer_page.submit_button()


def test_logout_page(browser):
    logout_page = LogOutPage(browser)
    logout_page.select_login_page()
